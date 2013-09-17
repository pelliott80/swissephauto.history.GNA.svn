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
vpath %.gif $(astrodocsrc)/doc
vpath %.htm $(astrodienst)/doc

pdfdir=${docdir}
htmldir=${docdir}
astrodocdir=${docdir}

SUFFIXES = .pdf .html .doc

EXTRA_DIST = $(astrodocsrc)/confirm-copywrite.email $(astrodocsrc)/LICENSE \
	     $(astrodocsrc)/swephprg.doc  $(astrodocsrc)/swisseph.doc


#if we can produce documentation i.e. pdf and html
if DOCS

html_DATA = swephprg.html  swisseph.html
pdf_DATA = swephprg.pdf   swisseph.pdf


#if we use loconvert to produce docs
if HAVE_LOCONVERT


#above was multi target build.
# see https://bugzilla.novell.com/show_bug.cgi?id=715856#c1
.NOTPARALLEL: 



swephprg.html: swephprg.doc
	loconvert --force $<  $@  || \
	loconvert --force $<  $@ 
	sleep 20
swisseph.html: swisseph.doc
	loconvert --force $<  $@  || \
	loconvert --force $<  $@
	sleep 20
swephprg.pdf: swephprg.doc
	loconvert --force $<  $@  || \
	loconvert --force $<  $@
	sleep 20
swisseph.pdf: swisseph.doc
	loconvert --force $<  $@ || \
	loconvert --force $<  $@
	sleep 20

endif

#if we use internal loconvert to produce docs
if HAVE_ILOCONVERT


#above was multi target build.
# see https://bugzilla.novell.com/show_bug.cgi?id=715856#c1
.NOTPARALLEL: 



swephprg.html: swephprg.doc
	../iloconvert/loconvert --force $<  $@  || \
	../iloconvert/loconvert --force $<  $@
	sleep 20
swisseph.html: swisseph.doc
	../iloconvert/loconvert --force $<  $@ || \
	../iloconvert/loconvert --force $<  $@
	sleep 20
swephprg.pdf: swephprg.doc
	../iloconvert/loconvert --force $<  $@ || \
	../iloconvert/loconvert --force $<  $@
	sleep 20
swisseph.pdf: swisseph.doc
	../iloconvert/loconvert --force $<  $@ || \
	../iloconvert/loconvert --force $<  $@
	sleep 20

endif


#if we use unoconv to produce documentation.
if HAVE_UNOCONV

#above was multi target build.
.NOTPARALLEL: 

$(html_DATA) $(pdf_DATA): swephprg.doc   swisseph.doc
#tricky code alert
#in a subshell save pid of subshell, ($$$$) becomes $$ in subshell.
#then exec the listener. result is listnener running detached with saved pid.
#create and save temp writeable directory to use by libreoffice
	echo $$(mktemp -d)>$@.home.dir
	echo "echo "'$$$$'" >$@.pid ; export HOME=$$(<$@.home.dir);exec unoconv --listener" | $(SHELL) &
	export HOME=$$(<$@.home.dir); \
	sleep 20; \
	for ext in html pdf ;do \
	   for name in swephprg  swisseph ; do \
	   		  echo "unoconv -o $${name}.$${ext} -f $${ext} $(astrodocsrc)/$${name}.doc " ;\
	   		  unoconv -o $${name}.$${ext} -f $${ext} $(astrodocsrc)/$${name}.doc  \
	   		  || \
	   		  unoconv -o $${name}.$${ext} -f $${ext} $(astrodocsrc)/$${name}.doc  ; \
	   done; \
	done
	-rm -r $$(<$@.home.dir)
	-rm $@.home.dir
#kill sub-sub process and sub-process
	for pid in $$(pgrep -P $$(<$@.pid) ) ; do \
                pkill -P $$pid; \
                kill $$pid ; \
        done
#kill the saved pid, i.e. the listener. $$ becomes $ in the shell.
	-kill $$(<$@.pid)
#remove the pid save file
	-rm $@.pid

swephprg.html: swephprg.doc
swisseph.html: swisseph.doc
swephprg.pdf: swephprg.doc
swisseph.pdf: swisseph.doc

endif

#if we use old unoconv to produce documentation.
if HAVE_OUNOCONV

#above was multi target build.
.NOTPARALLEL: 

$(html_DATA) $(pdf_DATA): swephprg.doc   swisseph.doc
#tricky code alert
#in a subshell save pid of subshell, ($$$$) becomes $$ in subshell.
#then exec the listener. result is listnener running detached with saved pid.
#create and save temp writeable directory to use by libreoffice
	echo $$(mktemp -d)>$@.home.dir
	echo "echo "'$$$$'" >$@.pid ; export HOME=$$(<$@.home.dir);exec unoconv --listener" | $(SHELL) &
	export HOME=$$(<$@.home.dir); \
	sleep 20; \
	for ext in html pdf ;do \
	   for name in swephprg  swisseph ; do \
	   		  echo "unoconv --stdout  -f $${ext} $(astrodocsrc)/$${name}.doc > $${name}.$${ext} " ;\
	   		  unoconv --stdout -f $${ext} $(astrodocsrc)/$${name}.doc > $${name}.$${ext} \
	   		  || \
	   		  unoconv --stdout -f $${ext} $(astrodocsrc)/$${name}.doc >  $${name}.$${ext}  ; \
	   done; \
	done
	-rm -r $$(<$@.home.dir)
	-rm $@.home.dir
#kill sub-sub process and sub-process
	for pid in $$(pgrep -P $$(<$@.pid) ) ; do \
                pkill -P $$pid; \
                kill $$pid ; \
        done
#kill the saved pid, i.e. the listener. $$ becomes $ in the shell.
	-kill $$(<$@.pid)
#remove the pid save file
	-rm $@.pid

swephprg.html: swephprg.doc
swisseph.html: swisseph.doc
swephprg.pdf: swephprg.doc
swisseph.pdf: swisseph.doc

endif

# use htmldoc to produce documentation.
if HAVE_HTMLDOC
swephprg.html:	$(astrodienst)/doc/swephprg.htm
	cp  $<  $@
swisseph.html:	$(astrodienst)/doc/swisseph.htm
	cp  $<  $@

%.pdf:	%.html
	htmldoc -f $@ --webpage $<

swephprg.pdf:	swephprg.html
swisseph.pdf:	swisseph.html

endif

endif

dist_astrodoc_DATA = $(astrodocsrc)/sweph.gif  $(astrodocsrc)/swephin.gif

CLEANFILES = $(html_DATA) $(pdf_DATA) *.pid *.home.dir
