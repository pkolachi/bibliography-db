#!/usr/bin/env python3

import io  ;
import os  ; 
import sys ;

try :
  import bibtexparser as bibp ; 
except ImportError :
  print("Required module bibtexparser is uninstalled.\nRun pip install bibtexparser", file=sys.stderr) ; 
  sys.exit(1) ; 

def main() :
  if len(sys.argv) < 4 :
    print("./{0} <preprints-bib> <published-bib> <out-pref>".format(sys.argv[0]), file=sys.stderr) ; 
    sys.exit(1) ; 

  INDNT_LEN = 4 ; 
  # process cmd-line arguments
  curpubbib = sys.argv[1] ;   # bib file of published articles on arxiv
  curprebib = sys.argv[2] ;   # bib file of pre-print articles on arxiv
  outpref   = sys.argv[3] ;   # output prefix
  arxivfpth = sys.argv[4] if len(sys.argv) > 4 else None ;  # path of folder with papers from arxiv 
  initpubfp = sys.argv[5] if len(sys.argv) > 5 else None ;  # init bib file if needed of published articles
  initprefp = sys.argv[6] if len(sys.argv) > 6 else None ;  # init bib file if needed of pre-print articles

  # set the parser settings (tune-up to fit my requirements)
  parserb = 
  # set the writer settings (tune-up to fit my requirements)
  writerb = bibp.BibtexWriter() ; 
  writerb.order_entries_by = ('id',)  # sort entries based on paper id for arxiv collection
  writerb.indent        = ' '*INDNT_LEN ;  # indent fields with 4 spaces (matches .vimrc settings)
  writerb.display_order = ('author', 'title', 'eprint', 'year', ) ;  # order fields in entry starting with these keys, followed by alphabetical order of the rest

  # make a database of existing entries
  pubbibdb = parserb.load(curpubbib) ; 
  prebibdb = parserb.load(curprebib) ;
  # prefix ids of all papers with ar-
  

  # if there are any new files in the <arxiv-folder> missing from bibfiles 
  # list them
  if arxivfpth : 
    paperids  = [os.path.splitext(fnm)[0] for fnm in os.listdir(arxivfpth)] ; 
    # strip version suffixes from paperids (e.g. 1904.04063v2)
    mpaperids = [pid for pid in paperids if pid not in bibdb] ;  # missing entries
    print("Arxiv paperids missing from all bib databases\t{0}".format(' '.join(mpaperids))) ; 
    
  return 0 ; 

if __name__ == '__main__' :
  main() ; 
