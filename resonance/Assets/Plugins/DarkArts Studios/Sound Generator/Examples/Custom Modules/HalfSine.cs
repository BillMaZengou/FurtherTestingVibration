using UnityEngine;

public class HalfSine : DarkArtsStudios.SoundGenerator.Module.BaseModule
{
    public static string MenuEntry() { return "Examples/Oscillator/Half Sine (C#)"; }

    public override float OnAmplitude(float frequency, float time, float duration, int depth)
    {
        float period = 1 / frequency;
        int numOfPeriod = (int)Mathf.Floor(time / period);
        time -= numOfPeriod * period;
        float x = Mathf.Deg2Rad * time * frequency * 360f;
        float pi = Mathf.Deg2Rad * 180f;

        if (x < pi)
        {
            return Mathf.Sin(x);
        }
        else
        {
            return 0.0f;
        }
    }
}