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

#do not distribute stuff distributed by astrodienst
# change add nodist
nodist_libswe_la_SOURCES = \
	swecl.c      \
	swedate.c      \
	swedate.h      \
	swedll.h      \
	swehel.c      \
	swehouse.c      \
	swehouse.h      \
	swejpl.c      \
	swejpl.h      \
	swemmoon.c      \
	swemplan.c      \
	swenut2000a.h      \
	sweodef.h      \
	swepcalc.c      \
	swepcalc.h      \
	swepdate.c      \
	sweph.c      \
	sweph.h      \
	swephexp.h      \
	swephlib.c      \
	swephlib.h
dist_libswe_la_SOURCES = \
	symbols.sym

libswe_la_LDFLAGS = \
	-lm         \
	-export-symbols symbols.sym


libswe_la_LIBADD = 

#do not distribute stuff distributed by astrodienst
# change add nodist
nodist_include_HEADERS = \
	$(astrosrc)/sweodef.h    \
	$(astrosrc)/swepcalc.h   \
	$(astrosrc)/swephexp.h

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = libswe-1.77.00.pc

EXTRA_DIST = \
	libswe-1.77.00.pc.in

#do not distribute stuff distributed by astrodienst
# change add nodist
nodist_EXTRA_DIST = \
	swemptab.c

bin_PROGRAMS = \
	swemini\
	swetest

#do not distribute stuff distributed by astrodienst
# change add nodist
nodist_swetest_SOURCES = \
	swetest.c

swetest_LDADD = \
	libswe.la

#do not distribute stuff distributed by astrodienst
# change add nodist
nodist_swemini_SOURCES = \
	swemini.c

swemini_LDADD = \
	libswe.la

#do not distribute stuff distributed by astrodienst
# change dist -> nodist
ephepkgdatadir = $(pkgdatadir)/users/ephe/
nodist_ephepkgdata_DATA = \
    $(astrosrc)/fixstars.cat\
    $(astrosrc)/sedeltat.txt.inactive\
    $(astrosrc)/sefstars.txt\
    $(astrosrc)/seleapsec.txt\
    $(astrosrc)/seorbel.txt



swedocdir = ${docdir}/../libswe-dev
#do not distribute stuff distributed by astrodienst
# change add nodist
nodist_swedoc_DATA = \
    $(astrosrc)/LICENSE\
    $(astrosrc)/swemini.c $(astrosrc)/swetest.c

