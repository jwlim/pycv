def FnImConvol( OriginImage, Kernel, Padding ) :
    "This function is to perform 2D convoluttion"
    
    ## Function Name: FnImConvol ******************************************
    #
    # Description: Function of 2D convolution
    # Author: Wonatek Lim ( lwt1849@gmail.com )
    # Copyright 2015 Wontaek Lim, All Right Reserved
    #
    # Input
    #  - OriginImage:  Image array
    #  - Kernel:       Kernel array
    #  - Padding:      Type of padding( 'zero', 'wrap', 'clamp', 'mirror' )
    #
    #***********************************************************************
    
    import math
    import sys
    import numpy as np
    
    # 1. Get ImageSize, KernelSize
    [ ImWidth, ImHeight] = OriginImage.shape;
    [ KerWidth, KerHeight] = Kernel.shape;
    
    NumLeftAddedCol = math.trunc(float(KerWidth)/2)
    NumRightAddedCol = math.trunc(float(KerWidth)/2)
    if ( KerWidth % 2 ) == 0:
        # Even number
        NumLeftAddedCol = NumLeftAddedCol - 1
    
    NumUpAddedRow = math.trunc(float(KerHeight)/2)
    NumDnAddedRow = math.trunc(float(KerHeight)/2)
    if ( KerHeight % 2 ) == 0:
    # Even number
        NumUpAddedRow = NumUpAddedRow - 1

    if KerWidth != KerHeight:
        print "Kernel should be square matrix!"
        sys.exit()


    # 2. Create padded image
    ExtendedCol = ImWidth+KerWidth-1
    ExtendedRow = ImHeight+KerHeight-1
    ExtendedImage = np.zeros( (ExtendedCol, ExtendedRow) )
    
    if Padding == 'wrap':
        ExtendedImage = np.lib.pad( OriginImage, (NumLeftAddedCol, NumRightAddedCol), 'wrap')
    
    elif Padding == 'clamp':
        ExtendedImage = np.lib.pad( OriginImage, (NumLeftAddedCol, NumRightAddedCol), 'edge')

    elif Padding == 'mirror':
        ExtendedImage = np.lib.pad( OriginImage, (NumLeftAddedCol, NumRightAddedCol), 'symmetric')

    else:
        ExtendedImage = np.lib.pad( OriginImage, (NumLeftAddedCol, NumRightAddedCol), 'constant', constant_values = (0,0) )
    
    
    # 3. 2D Convolution
    FilteredImage = np.zeros( (ImWidth, ImHeight) ) # Create result array
    for ImageIndexX in range(ImWidth):
        ExImageIndexX = ImageIndexX + NumLeftAddedCol

        for ImageIndexY in range(ImHeight):
            ExImageIndexY = ImageIndexY + NumUpAddedRow

            ObjImg = ExtendedImage[ ( ExImageIndexX-NumLeftAddedCol ):( ExImageIndexX+NumRightAddedCol+1),
                                   ( ExImageIndexY-NumUpAddedRow ):( ExImageIndexY+NumDnAddedRow+1 )]

            AccumedValue = np.sum( np.multiply( ObjImg, Kernel ) )

            # Update value
            FilteredImage[ImageIndexX, ImageIndexY] = AccumedValue

    return FilteredImage