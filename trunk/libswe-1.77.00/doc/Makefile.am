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
## File created by the gnome-build tools


vpath %.doc $(astrodocsrc)
vpath %.gif $(astrodienst)/doc

pdfdir=${docdir}
htmldir=${docdir}
astrodocdir=${docdir}

SUFFIXES = .pdf .html .doc





#above was multi target build.
.NOTPARALLEL: 

html_DATA = swephprg.html  swisseph.html
pdf_DATA = swephprg.pdf   swisseph.pdf

$(html_DATA) $(pdf_DATA): swephprg.doc   swisseph.doc
#tricky code alert
#in a subshell save pid of subshell, ($$$$) becomes $$ in subshell.
#then exec the listener. result is listnener running detached with saved pid.
	echo "echo "'$$$$'" >$@.pid ; exec unoconv --listener" | $(SHELL) &
	for ext in html pdf ;do \
	   for name in swephprg  swisseph ; do \
	   		  echo "unoconv --stdout -f $${ext} $(astrodocsrc)/$${name}.doc   >  $${name}.$${ext}" ;\
	   		  unoconv --stdout -f $${ext} $(astrodocsrc)/$${name}.doc   >  $${name}.$${ext} \
	   		  || \
	   		  unoconv --stdout -f $${ext} $(astrodocsrc)/$${name}.doc   >  $${name}.$${ext} ; \
	   done; \
	done
#kill the saved pid, i.e. the listener. $$ becomes $ in the shell.
	-kill $$(<$@.pid)
#remove the pid save file
	-rm $@.pid

swephprg.html: swephprg.doc
swisseph.html: swisseph.doc
swephprg.pdf: swephprg.doc
swisseph.pdf: swisseph.doc

#swephprg_html_SOURCES = swephprg.doc

#swisseph_html_SOURCES = swisseph.doc

#swephprg_pdf_SOURCES = swephprg.doc

#swisseph_pdf_SOURCES = swisseph.doc

#do not distribute stuff distributed by astrodienst
# change add nodist
nodist_astrodoc_DATA = $(astrodienst)/doc/sweph.gif  $(astrodienst)/doc/swephin.gif

CLEANFILES = $(html_DATA) $(pdf_DATA) *.pid
