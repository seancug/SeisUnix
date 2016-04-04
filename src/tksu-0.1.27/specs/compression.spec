# compression.spec --
#
#	Tksu compression category modules.
#	See README.spec for a description of the spec file format.
#
# CVS: $id$

[dctcomp]

Cat:	Compression
Desc:	compression by discrete cosine transform
Port:	stdin bin r req		input containing floats
Port:	stdout bin w req	output containing floats
Port:	par par r -		optional par file input
Param:	n1 int 1<= req		number of samples in fast (first) dimension
Param:	n2 int 1<= req		number of samples in slow (second) dimension
Param:	blocksize1 int 1<= 16	blocksize in direction 1
Param:	blocksize2 int 1<= 16	blocksize in direction 2
Param:	error float 0< 0.01	acceptable error

[dctuncomp]

Cat:	Compression
Desc:	discrete cosine transform uncompression
Port:	stdin bin r req		input containing floats
LDesc:	The input must be a file compressed by dctcomp.
Port:	stdout bin w req	output containing floats

[supack1]

Cat:	Compression
Desc:	pack trace samples from floats to 1-byte chars
Port:	stdin su r req		input traces
Port:	stdout su w req		output traces, with trid = CHARPACK
LDesc:	ungpow and unscale are stored in trace header for use by suunpack1
Port:	par par r -		optional par file input
Param:	gpow float 0< 0.5	exponent used to compress sample dynamic range

[suunpack1]

Cat:	Compression
Desc:	unpack trace samples from 1-byte chars to floats
Port:	stdin su r req		input traces generated by supack1
Port:	stdout su w req		output traces

[supack2]

Cat:	Compression
Desc:	pack trace samples from floats to 2-byte ints
Port:	stdin su r req		input traces
Port:	stdout su w req		output traces, with trid = SHORTPACK
LDesc:	ungpow and unscale are stored in trace header for use by suunpack1
Port:	par par r -		optional par file input
Param:	gpow float 0< 0.5	exponent used to compress sample dynamic range

[suunpack2]

Cat:	Compression
Desc:	unpack trace samples from 2-byte ints to floats
Port:	stdin su r req		input traces generated by supack2
Port:	stdout su w req		output traces

[wpc1comp2]

Cat:	Compression
Desc:	compress 2D seismic section in fast dimension using wavelets
Port:	stdin bin r req		headerless input traces
Port:	stdout bin w req	compressed array of floats
Port:	par par r -		optional par file input
Param:	n1 int 1<= req		number of samples in each trace
Param:	error float 0< 0.01	relative RMS error allowed in compression

[wpc1uncomp2]

Cat:	Compression
Desc:	uncompress 2D seismic section that has been compressed with wpc1comp2
Port:	stdin bin r req		compressed array generated by wpc1comp2
Port:	stdout bin w req	uncompressed headerless output traces

[wpccompress]

Cat:	Compression
Desc:	compress 2D seismic section in both dimensions using wavelets
Port:	stdin bin r req		headerless input traces
Port:	stdout bin w req	compressed array of floats
Port:	par par r -		optional par file input
Param:	n1 int 1<= req		number of samples in fast dimension
Param:	n2 int 1<= req		number of samples in slow dimension
Param:	error float 0< 0.01	relative RMS error allowed in compression

[wpcuncompress]

Cat:	Compression
Desc:	uncompress 2D seismic section that has been compressed with wpccompress
Port:	stdin bin r req		compressed array generated by wpccompress
Port:	stdout bin w req	uncompressed headerless output traces

[wptcomp]

Cat:	Compression
Desc:	compress 2D section by WPT (wavelet packet transform)
Port:	stdin bin r req		headerless input traces
Port:	stdout bin w req	compressed array of floats
Port:	par par r -		optional par file input
Param:	n1 int 1<= req		number of samples in fast (1st) dimension
Param:	n2 int 1<= req		number of samples in slow (2nd) dimension
Param:	nfilter1 int 1<= 11	number of filters in direction 1
Param:	nfilter2 int 1<= 11	number of filters in direction 2
Param:	nstage1 int 1<= -	filter stages in direction 1
Param:	nstage2 int 1<= -	filter stages in direction 2
Param:	error float 0< 0.01	relative RMS error allowed in compression

[wptuncomp]

Cat:	Compression
Desc:	uncompress 2D section that has been WPT compressed
Port:	stdin bin r req		compressed array generated by wptcomp
Port:	stdout bin w req	uncompressed headerless output traces

[wtcomp]

Cat:	Compression
Desc:	compress 2D section by WT (wavelet transform)
Port:	stdin bin r req		headerless input traces
Port:	stdout bin w req	compressed array of floats
Port:	par par r -		optional par file input
Param:	n1 int 1<= req		number of samples in fast (1st) dimension
Param:	n2 int 1<= req		number of samples in slow (2nd) dimension
Param:	nfilter int 1<= 11	number of filters
Param:	nstage1 int 1<= -	filter stages in direction 1
Param:	nstage2 int 1<= -	filter stages in direction 2
Param:	error float 0< 0.01	relative RMS error allowed in compression

[wtuncomp]

Cat:	Compression
Desc:	uncompress 2D section that has been WT compressed
Port:	stdin bin r req		compressed array generated by wtcomp
Port:	stdout bin w req	uncompressed headerless output traces
