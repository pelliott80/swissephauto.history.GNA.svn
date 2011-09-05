dnl Copyright Paul Elliott 2011
dnl
dnl
dnl  This file is part of libswe for GNU/LINUX.
dnl
dnl    swelib for GNU/LINUX is free software: you can redistribute it and/or modif
dnl    it under the terms of the GNU General Public License as published by
dnl    the Free Software Foundation, either version 2 of the License, or
dnl    (at your option) any later version.
dnl
dnl    libswe is distributed in the hope that it will be useful,
dnl    but WITHOUT ANY WARRANTY; without even the implied warranty of
dnl    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
dnl    GNU General Public License for more details.
dnl
dnl    You should have received a copy of the GNU General Public License
dnl    along with lib.  If not, see <http://www.gnu.org/licenses/>.
dnl Process this file with autoconf to produce a configure script.
dnl Created by Anjuta application wizard.

AC_INIT(libswe, 1.77.00.0001)
m4_ifdef([AM_SILENT_RULES],[AM_SILENT_RULES([yes])])

AM_INIT_AUTOMAKE(AC_PACKAGE_NAME, AC_PACKAGE_VERSION)
AC_CONFIG_HEADERS([config.h])
AM_MAINTAINER_MODE

AC_PROG_CC

AC_ARG_VAR(WPCONVERT, [word processing conversion program, loconvert or unoconv])

AC_CHECK_PROGS(WPCONVERT,[loconvert unoconv])

AM_CONDITIONAL(HAVE_LOCONVERT,[test "x$WPCONVERT" == "xloconvert"])
AM_CONDITIONAL(HAVE_UNOCONV,[test "x$WPCONVERT" == "xunoconv"])


astrodienst='$(top_builddir)/astrodienst'
AC_SUBST(astrodienst)


dnl When upstream releases documentation source
dnl in right place, this will be
dnl $(astrodienst)/doc
astrodocsrc='$(top_builddir)/astrodocsrc'
AC_SUBST(astrodocsrc)


AC_CHECK_LIB([m],[cos])
AC_CHECK_LIB([m],[log10])
AC_CHECK_LIB([m],[atan2])
AC_CHECK_LIB([m],[log])
AC_CHECK_LIB([m],[atan])
AC_CHECK_LIB([m],[pow])
AC_CHECK_LIB([m],[sin])
AC_CHECK_LIB([m],[exp])
AC_CHECK_LIB([m],[acos])
AC_CHECK_LIB([m],[asin])
AC_CHECK_LIB([m],[tan])
AC_CHECK_LIB([m],[trunc])
AC_CHECK_LIB([m],[sqrt])
AC_CHECK_LIB([m],[sincos])
AC_CHECK_LIB([m],[fmod])
AC_CHECK_LIB([m],[floor])



AM_PROG_LIBTOOL





AC_OUTPUT([
Makefile
src/libswe-1.77.00.pc
src/Makefile
doc/Makefile
])
