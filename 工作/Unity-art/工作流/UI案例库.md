### Component相关

1. 不需要接收点击事件的图/文字，去除Raycast Target
2. setting下有很多选择项，需要依次排列。可以使用Content Size Fitter + Vertical Layout Group
3. 多语言使用LocalizationText，文字加阴影不属于LocalizationText，新写一个脚本，使用组合的方式扩展。
4. 网图使用CacheImage，不满足需求情况下提出新需求而不是使用RawImage，这样会导致不在图片内存管理框架中

