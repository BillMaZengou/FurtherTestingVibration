using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class player : MonoBehaviour
{
    private AudioClip Sound;
    private GameObject SoundType;
    private GameObject SoundPlayer;
    private AudioSource audioSource;

    public GameObject symmetricWave;

    private int counter;

    // Start is called before the first frame update
    void Start()
    {
        SoundPlayer = GameObject.Find("Audio Source");
        audioSource = SoundPlayer.GetComponent<AudioSource>();
        counter = 0;
    }

    public void Play()
    {
        SoundType = symmetricWave;
        FindSound();
        PlaySound();
    }

    public void Stop()
    {
        audioSource.Stop();
    }

    private void PlaySound()
    {
        audioSource.Stop();
        audioSource.loop = true;
        audioSource.clip = Sound;
        audioSource.volume = 1.0f;
        audioSource.Play();
    }

    private void FindSound()
    {
        DarkArtsStudios.SoundGenerator.Composition bounceComposition = SoundType.GetComponent<DarkArtsStudios.SoundGenerator.Composition>();
        DarkArtsStudios.SoundGenerator.Module.Output output = null;
        foreach (DarkArtsStudios.SoundGenerator.Module.BaseModule module in bounceComposition.modules)
        {
            if (module.GetType() == typeof(DarkArtsStudios.SoundGenerator.Module.Output))
            {
                output = module as DarkArtsStudios.SoundGenerator.Module.Output;
                break;
            }
        }
        if (output)
        {
            output.Generate();
            Sound = output.audioClip;
        }
    }
}
