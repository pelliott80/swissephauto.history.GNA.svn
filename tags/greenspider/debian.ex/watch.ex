# Example watch control file for uscan
# Rename this file to "watch" and then you can run the "uscan" command
# to check for upstream updates and more.
# See uscan(1) for format

# Compulsory line, this is a version 3 file
version=3

# Uncomment to examine a Webpage
# <Webpage URL> <string match>
#http://www.example.com/downloads.php libswe-(.*)\.tar\.gz

# Uncomment to examine a Webserver directory
#http://www.example.com/pub/libswe-(.*)\.tar\.gz

# Uncommment to examine a FTP server
#ftp://ftp.example.com/pub/libswe-(.*)\.tar\.gz debian uupdate

# Uncomment to find new files on sourceforge, for devscripts >= 2.9
# http://sf.net/libswe/libswe-(.*)\.tar\.gz

# Uncomment to find new files on GooglePages
# http://example.googlepages.com/foo.html libswe-(.*)\.tar\.gz

# The option downloadurlmangle can be used to mangle the URL of the file
# to download.  This can only be used with http:// URLs.  This may be
# necessary if the link given on the webpage needs to be transformed in
# some way into one which will work automatically, for example:
#opts=downloadurlmangle=s/prdownload/download/ \
#http://developer.berlios.de/project/showfiles.php?group_id=12390 \
#http://prdownload.berlios.de/softdevice/libswe-(.*).tar.gz



# This is the format for an FTP site:
# Full-site-with-pattern  [Version  [Action]]

#opts=filenamemangle=s/swe_unix_src_(.*)\.tar\.gz/libswe_$1\.orig-astrodienst\.tar\.gz/ \
#ftp://ftp.astro.com/pub/swisseph/swe_unix_src_(.*)\.tar\.gz \
#debian 

