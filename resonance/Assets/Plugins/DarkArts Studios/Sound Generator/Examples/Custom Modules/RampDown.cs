using UnityEngine;

public class RampDown : DarkArtsStudios.SoundGenerator.Module.BaseModule
{
    public static string MenuEntry() { return "Examples/Oscillator/Ramp Down (C#)"; }

    public override void InitializeAttributes()
    {
        Attribute ammount_of_asymmetry = new Attribute("Amount of Asymmetry", 0.0f);
        ammount_of_asymmetry.type = Attribute.AttributeType.SLIDER;
        ammount_of_asymmetry.clampMinimum = true;
        ammount_of_asymmetry.clampMinimumValue = 0.0f;
        ammount_of_asymmetry.clampMaximum = true;
        ammount_of_asymmetry.clampMaximumValue = 50.0f;
        attributes.Add(ammount_of_asymmetry);
    }

    public override float OnAmplitude(float frequency, float time, float duration, int depth)
    {
        float alpha = attribute("Amount of Asymmetry").value / 100f;
        float period = 1.0f / frequency;
        int numOfPeriod = (int)Mathf.Floor(time / period);
        time -= numOfPeriod * period;
        float x = Mathf.Deg2Rad * time * frequency * 360f;
        float pi = Mathf.Deg2Rad * 180f;

        if (x < 2.0f * alpha * pi)
        {
            return 1.0f;
        }
        else
        {
            return (-x / pi + 1.0f + alpha) / (1 - alpha);
        }
    }
}
