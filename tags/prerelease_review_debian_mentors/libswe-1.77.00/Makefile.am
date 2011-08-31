# Copyright Paul Elliott 2011
#
#
#This file is part of libswe for GNU/LINUX.
#
#    swelib is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    libswe for GNU/LINUX is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with lib.  If not, see <http://www.gnu.org/licenses/>.
## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = src \
	doc


swedocdir = ${docdir}/../libswe-dev
swedoc_DATA = \
	README\
	COPYING\
	AUTHORS\
	ChangeLog\
	INSTALL\
	NEWS

man_MANS = libswe.3 swetest.1 swemini.1

EXTRA_DIST = $(man_MANS) $(swedoc_DATA)


# Remove doc directory on uninstall
uninstall-local:
	-rm -r $(swedocdir)
