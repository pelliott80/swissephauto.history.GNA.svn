# Copyright Paul Elliott 2011
#
#
#This file is part of libswe for GNU/LINUX.
#
#    swelib for GNU/LINUX is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    libswe is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with lib.  If not, see <http://www.gnu.org/licenses/>.
## Process this file with automake to produce Makefile.in

## Created by Anjuta

AM_CPPFLAGS = \
	-DPACKAGE_LOCALE_DIR=\""$(prefix)/$(DATADIRNAME)/locale"\" \
	-DPACKAGE_SRC_DIR=\""$(srcdir)"\" \
	-DPACKAGE_DATA_DIR=\""$(datadir)"\" 

AM_CFLAGS =\
	 -Wall\
	 -g

astrosrc = $(astrodienst)/src
vpath %.c $(astrosrc)
vpath %.h $(astrosrc)
vpath %.cat $(astrosrc)
vpath %.txt $(astrosrc)
vpath %.inactive $(astrosrc)
vpath LICENSE $(astrosrc)


lib_LTLIBRARIES = libswe.la

dist_libswe_la_SOURCES = \
	$(astrosrc)/swecl.c      \
	$(astrosrc)/swedate.c      \
	$(astrosrc)/swedate.h      \
	$(astrosrc)/swedll.h      \
	$(astrosrc)/swehel.c      \
	$(astrosrc)/swehouse.c      \
	$(astrosrc)/swehouse.h      \
	$(astrosrc)/swejpl.c      \
	$(astrosrc)/swejpl.h      \
	$(astrosrc)/swemmoon.c      \
	$(astrosrc)/swemplan.c      \
	$(astrosrc)/swenut2000a.h      \
	$(astrosrc)/sweodef.h      \
	$(astrosrc)/sweph.c      \
	$(astrosrc)/sweph.h      \
	$(astrosrc)/swephexp.h      \
	$(astrosrc)/swephlib.c      \
	$(astrosrc)/swephlib.h

#-version info calculation
# v1.77.0 was first therefore -version-info 0:0:0
# v1.78.0 added, but no mod deleted interface os
#                             -version-info 1:0:1
# v1.79.0 added, but no mod deleted interface os
#                             -version-info 2:0:2
# v1.80.0 addeded but deleted no interface or mod
#			      -version-info 3:0:3

libswe_la_LDFLAGS = \
	-version-info 3:0:3 \
	-lm         \
	-export-symbols-regex ^swe_


libswe_la_LIBADD = 

dist_include_HEADERS = \
	$(astrosrc)/sweodef.h    \
	$(astrosrc)/swephexp.h

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = libswe-1.80.00.pc

EXTRA_DIST = \
	libswe-1.80.00.pc.in	    \
	$(astrosrc)/swepcalc.c      \
	$(astrosrc)/swepcalc.h      \
	$(astrosrc)/swepdate.c      \
	$(astrosrc)/swemptab.c

bin_PROGRAMS = \
	swemini\
	swetest

dist_swetest_SOURCES = \
	$(astrosrc)/swetest.c

swetest_LDADD = \
	libswe.la

dist_swemini_SOURCES = \
	$(astrosrc)/swemini.c

swemini_LDADD = \
	libswe.la

ephedatadir = $(pkgdatadir)/ephe/


dist_ephedata_DATA = \
    $(astrosrc)/fixstars.cat\
    $(astrosrc)/sedeltat.txt.inactive\
    $(astrosrc)/sefstars.txt\
    $(astrosrc)/seleapsec.txt\
    $(astrosrc)/seorbel.txt



swedocdir = ${docdir}
dist_swedoc_DATA = \
    $(astrosrc)/swemini.c $(astrosrc)/swetest.c \
    $(astrosrc)/LICENSE

