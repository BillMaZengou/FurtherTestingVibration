using UnityEngine;

public class TwoStepsFunction : DarkArtsStudios.SoundGenerator.Module.BaseModule
{
    public static string MenuEntry() { return "Examples/Oscillator/HapCube (C#)"; }

    public override void InitializeAttributes()
    {
        Attribute firstStep = new Attribute("First Step", 33.0f);
        firstStep.type = Attribute.AttributeType.SLIDER;
        firstStep.clampMinimum = true;
        firstStep.clampMinimumValue = 0.0f;
        firstStep.clampMaximum = true;
        firstStep.clampMaximumValue = 50.0f;
        attributes.Add(firstStep);

        Attribute firstValue = new Attribute("First Value", 1.0f);
        firstValue.type = Attribute.AttributeType.SLIDER;
        firstValue.clampMinimum = true;
        firstValue.clampMinimumValue = 0.0f;
        firstValue.clampMaximum = true;
        firstValue.clampMaximumValue = 1.0f;
        attributes.Add(firstValue);

        Attribute secondStep = new Attribute("Second Step", 33.0f);
        secondStep.type = Attribute.AttributeType.SLIDER;
        secondStep.clampMinimum = true;
        secondStep.clampMinimumValue = 0.0f;
        secondStep.clampMaximum = true;
        secondStep.clampMaximumValue = 50.0f;
        attributes.Add(secondStep);

        Attribute secondValue = new Attribute("Second Value", 1.0f);
        secondValue.type = Attribute.AttributeType.SLIDER;
        secondValue.clampMinimum = true;
        secondValue.clampMinimumValue = 0.0f;
        secondValue.clampMaximum = true;
        secondValue.clampMaximumValue = 1.0f;
        attributes.Add(secondValue);
    }

    public override float OnAmplitude(float frequency, float time, float duration, int depth)
    {
        float alpha = attribute("First Step").value / 100f;
        float beta = attribute("Second Step").value / 100f;
        float firstValue = attribute("First Value").value;
        float secondValue = attribute("Second Value").value;
        float period = 1 / frequency;
        int numOfPeriod = (int)Mathf.Floor(time / period);
        time -= numOfPeriod * period;
        float x = Mathf.Deg2Rad * time * frequency * 360f;
        float pi = Mathf.Deg2Rad * 180f;

        if (x < 2.0f * alpha * pi)
        {
            return firstValue;
        }
        else if (x < 2.0f * (alpha+beta) * pi)
        {
            return secondValue;
        }
        else
        {
            return 0.0f;
        }
    }
}
