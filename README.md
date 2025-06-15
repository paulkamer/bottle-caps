# Duplicate image detector for the Raspberry Pi

Hobby project to detect duplicate images using the Raspberry Pi camera module and (optionally) the Sense HAT.

Using this for my modest collection of beer bottle caps, to prevent adding duplicates.


```mermaid
flowchart LR
    Start --> CountDown
    CountDown --> TakePhoto
    TakePhoto --> DetectDuplicates
    DetectDuplicates --> ReportStatus
    ReportStatus --> End
```


## TODO's

Bottlecaps project
- [x] support input from Sense HAT
- [x] Support override of `duplicate-image-detector config.ini`
- [ ] Allow retaking photo
- [ ] simplify feedback presented by Sense HAT (Green/Orange/Red)
- [ ] use events to display messages on Sense HAT
- [ ] Rely on color histogram in case of many similarities


## Sources
https://pythonhosted.org/sense-hat/