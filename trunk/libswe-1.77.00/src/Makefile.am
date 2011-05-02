# Copyright Paul Elliott 2011
#
#
#This file is part of libswe.
#
#    swelib is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
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

lib_LTLIBRARIES = libswe.la


libswe_la_SOURCES = \
	swephlib.h \
	swephlib.c \
	swephexp.h \
	sweph.h \
	sweph.c \
	swepdate.c \
	swepcalc.h \
	swepcalc.c \
	sweodef.h \
	swenut2000a.h \
	swemplan.c \
	swemmoon.c \
	swejpl.h \
	swejpl.c \
	swehouse.h \
	swehouse.c \
	swehel.c \
	swedll.h \
	swedate.h \
	swedate.c \
	swecl.c

libswe_la_CFLAGS = \
	-lm

libswe_la_LDFLAGS = 
# add to above  -version-info 1:0:0 or whatever to control version info.

libswe_la_LIBADD = 

include_HEADERS = \
	swephexp.h\
	sweodef.h

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = libswe-1.77.0.pc

EXTRA_DIST = \
	libswe-1.77.0.pc.in\
	swemptab.c\
	LICENSE

bin_PROGRAMS = \
	swetest\
	swemini

swemini_SOURCES = \
	swemini.c

swemini_LDADD = \
	libswe.la

swetest_SOURCES = \
	swetest.c

swetest_LDADD = \
	libswe.la
dist_pkgdata_DATA = \
    fixstars.cat\
    sedeltat.txt.inactive\
    sefstars.txt\
    seleapsec.txt\
    seorbel.txt

# built files that come with the upstream tarball!
MOSTLYCLEANFILES = \
	libswe.a libswe.so \
	swetest \
	swecl.o    swehel.o    swejpl.o    swemplan.o  swepdate.o  sweph.o\
	swedate.o  swehouse.o  swemmoon.o  swepcalc.o  swephlib.o  swetest.o

swedocdir = ${prefix}/doc/swe
swedoc_DATA = \
    LICENSE