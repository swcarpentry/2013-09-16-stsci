#Astronomy Specific Examples

by Azalee Bostroem and Justin Ely

##Modules and functions covered:

###pyfits:   
	* open (.data, .header)   
	* getdata, getheader, getval   
	*  writeto   
	* multi-extension fits binary tables: .columns, .names, getting a column

###matplotlib:   
     * plot   
     * imshow (no axis object)   
     * label axes, title   
     * save

###numpy:   
     * arrays   
     * where   
     * sort, argsort   
     * max,min   
     * polyfit (polyval)   
     * interp   
     * sum (axis = )   

###scipy:
 
     * tstd   
     * mention: fft, signal, stats

###astropy.io   
	* asciitable

##Lesson Outline

1. Intro to numpy: arrays, where (with bitwise &), max, min, argsort, mean, standard deviation, astropy.io.asciitable   
* EX: TBD
2. Read STIS image, imshow, get all negative pix, set equal to 0, write output   
* EX: Read in a STIS image, set all pixels greater than 10 times the mean of the image to 0 (remove Hot Pixels and Cosmic Rays)   
3. Read COS spectrum (1105), plot wavelength vs flux, add labels, polyfit, overplot, add legend   
* EX.Read in a COS spectrum, use the where function to exclude certain wavelengths, fit continuum, save file   

