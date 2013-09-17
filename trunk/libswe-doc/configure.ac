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

AC_INIT(libswe-doc, 1.79.00.0001)
m4_ifdef([AM_SILENT_RULES],[AM_SILENT_RULES([yes])])

AM_INIT_AUTOMAKE([dist-bzip2 no-dist-gzip])
AC_CONFIG_HEADERS([config.h])
AM_MAINTAINER_MODE



# choose method to produce documentation. loconvert or unoconv
AC_ARG_VAR(WPCONVERT, [word processing conversion program, loconvert or unoconv])

AC_CHECK_PROGS(WPCONVERT,[loconvert unoconv htmldoc])

AM_CONDITIONAL(HAVE_LOCONVERT,[test "x$WPCONVERT" == "xloconvert"])
AM_CONDITIONAL(HAVE_ILOCONVERT,[test "x$WPCONVERT" == "xiloconvert"])
AM_CONDITIONAL(HAVE_UNOCONV,[test "x$WPCONVERT" == "xunoconv"])
AM_CONDITIONAL(HAVE_OUNOCONV,[test "x$WPCONVERT" == "xounoconv"])
AM_CONDITIONAL(HAVE_HTMLDOC,[test "x$WPCONVERT" == "xhtmldoc"])

#disable if impossible to produce documentation.
AC_ARG_ENABLE([docs], [  --enable-docs		disable when creating docs is impossible])
AM_CONDITIONAL(DOCS,[test "x$enable_docs" != "xno"])



ephedatadir='$(pkgdatadir)/ephe'
AC_SUBST(ephedatadir)


dnl When upstream releases documentation source
dnl in right place, this will be
dnl $(astrodienst)/doc
astrodocsrc='$(top_builddir)/astrodocsrc'
AC_SUBST(astrodocsrc)





AC_OUTPUT([
Makefile
doc/Makefile
])
