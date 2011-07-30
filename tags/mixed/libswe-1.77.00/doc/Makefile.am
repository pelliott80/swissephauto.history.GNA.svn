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
## File created by the gnome-build tools

dist_doc_DATA = sweph.gif  swephin.gif
html_DATA = swephprg.html  swisseph.html
pdf_DATA = swephprg.pdf   swisseph.pdf

EXTRA_DIST = ../srcdoc/swephprg.doc  ../srcdoc/swisseph.doc

swephprg.pdf:	../srcdoc/swephprg.doc
	$(LN_S) ../srcdoc/swephprg.doc ./swephprg.doc
	unoconv --listener &
	sleep 2
	unoconv -f pdf swephprg.doc  ||{ rm -f swephprg.doc;sleep 2; unoconv -f pdf swephprg.doc   }
	rm -f swephprg.doc

swisseph.pdf:	../srcdoc/swisseph.doc
	$(LN_S) ../srcdoc/swisseph.doc ./swisseph.doc
	unoconv --listener & 
	sleep 2
	unoconv -f pdf swisseph.doc ||{ rm -f swisseph.doc;sleep 2; unoconv -f pdf swephprg.doc   }
	rm -f swisseph.doc

swephprg.html:	../srcdoc/swephprg.doc
	$(LN_S) ../srcdoc/swephprg.doc ./swephprg.doc
	unoconv --listener & 
	sleep 2
	unoconv -f html swephprg.doc  ||{ rm -f swephprg.doc ;sleep 2; unoconv -f pdf swephprg.doc   }
	rm -f swephprg.doc

swisseph.html:		../srcdoc/swisseph.doc
	$(LN_S) ../srcdoc/swisseph.doc ./swisseph.doc
	unoconv --listener & 
	sleep 2
	unoconv -f html swisseph.doc  ||{ rm -f swisseph.doc ;sleep 2; unoconv -f pdf swephprg.doc   }
	rm -f swisseph.doc

#.htm comes with the upstream
CLEANFILES = swephprg.html  swisseph.html swephprg.pdf   swisseph.pdf\
    swephprg.doc swisseph.doc swephprg.htm  swisseph.htm
DISTCLEANFILES = swephprg.htm  swisseph.htm