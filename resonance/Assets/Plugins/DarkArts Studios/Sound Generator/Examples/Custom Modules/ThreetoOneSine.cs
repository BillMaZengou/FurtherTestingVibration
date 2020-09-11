using UnityEngine;

public class ThreetoOneSine : DarkArtsStudios.SoundGenerator.Module.BaseModule
{
    public static string MenuEntry() { return "Examples/Oscillator/ThreetoOneSine (C#)"; }

    public override float OnAmplitude(float frequency, float time, float duration, int depth)
    {
        float period = 1 / frequency;
        int numOfPeriod = (int)Mathf.Floor(time / period);
        if (numOfPeriod % 2 == 0) {
            return Mathf.Abs(Mathf.Sin(Mathf.Deg2Rad * time * frequency * 360f));
        }
        else {
            return Mathf.Sin(Mathf.Deg2Rad * time * frequency * 360f);
        }
    }
}
