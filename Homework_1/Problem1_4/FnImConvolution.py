def FnImConvol( OriginImage, Kernel ) :
    "This function is to perform 2D convoluttion"
    
    import math
    from numpy import*
    import numpy as np
    
    # 1. Get ImageSize, KernelSize
    [ ImWidth, ImHeight] = OriginImage.shape;
    [ KerWidth, KerHeight] = Kernel.shape;
    
    HalfWidthKernel = math.ceil( KerWidth/2 )
    HalfHeightKernel = math.ceil( KerHeight/2 )
    
    # 2. Create result array
    FilteredImage = np.zeros( (ImWidth, ImHeight) )
    
    # 3. Convolution
    for ImageIndexX in range(ImWidth):
        for ImageIndexY in range(ImHeight):
            
            AccumedValue = 0.0
            
            for KernelIndexX in range(KerWidth):
                ConvImIndexX = int( ImageIndexX - HalfWidthKernel + KernelIndexX )

                for KernelIndexY in range(KerHeight):
                    ConvImIndexY = int( ImageIndexY - HalfHeightKernel + KernelIndexY )
    
                    if (ConvImIndexX >= 0 ) and (ConvImIndexY >= 0) and (ConvImIndexX < ImWidth) and (ConvImIndexY < ImHeight):
                        SumVal = OriginImage[ConvImIndexX, ConvImIndexY] * Kernel[KernelIndexX, KernelIndexY]
                        AccumedValue = AccumedValue + SumVal
        
            # Update value
            FilteredImage[ImageIndexX, ImageIndexY] = AccumedValue


    return FilteredImage