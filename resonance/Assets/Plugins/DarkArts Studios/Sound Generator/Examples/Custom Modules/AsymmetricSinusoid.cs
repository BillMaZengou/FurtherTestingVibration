using UnityEngine;

public class AsymmetricSinusoid : DarkArtsStudios.SoundGenerator.Module.BaseModule
{
	public static string MenuEntry() { return "Examples/Oscillator/Asymmetric Sinusoid (C#)"; }

    public override void InitializeAttributes()
    {
        Attribute ammount_of_asymmetry = new Attribute("Amount of Asymmetry", 1.0f);
        ammount_of_asymmetry.type = Attribute.AttributeType.SLIDER;
        ammount_of_asymmetry.clampMinimum = true;
        ammount_of_asymmetry.clampMinimumValue = 1.0f;
        ammount_of_asymmetry.clampMaximum = true;
        ammount_of_asymmetry.clampMaximumValue = 25.0f;
        attributes.Add(ammount_of_asymmetry);

        Attribute amplified = new Attribute("Amplify", 1.0f);
        amplified.type = Attribute.AttributeType.SLIDER;
        amplified.clampMinimum = true;
        amplified.clampMinimumValue = 1.0f;
        amplified.clampMaximum = true;
        amplified.clampMaximumValue = 10.0f;
        attributes.Add(amplified);
    }

    public override float OnAmplitude(float frequency, float time, float duration, int depth)
	{
        int ammount_of_asymmetry = (int)attribute("Amount of Asymmetry").value;
        float amplified = attribute("Amplify").value;
        float x = Mathf.Deg2Rad * time * frequency * 360f;
        float result = SineElement(1.0f, ammount_of_asymmetry, x);

        for (int idx = 2; idx <= ammount_of_asymmetry; idx++) {
            result += SineElement(idx, ammount_of_asymmetry, x);
        }
        result *= amplified;
        return result;
	}

    private float Factorial(float number)
    {
        if (number == 1 || number == 0) {
            return 1;
        }
        return number * Factorial(number - 1);
    }

    private float SineElement(float idx, float total, float x)
    {
        float n_fac = Factorial(total);
        float nMk_fac = Factorial(total - idx);
        float nPk_fac = Factorial(total + idx);
        return (n_fac * n_fac) / (nMk_fac * nPk_fac) * (Mathf.Sin(idx * x) / idx);
    }
}
