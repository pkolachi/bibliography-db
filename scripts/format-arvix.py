#!/usr/bin/env python3


def read_biblines(bbls) :
  bufls = [] ; 
  for l in bbls :
    if l.startswith('@') : 
      bufls.append(l.strip()) ; 
    elif l.strip() == '}':
      bufls.append(l.strip()) ; 
      yield bufls ;
      bufls = [] ; 
    elif not l.strip() :
      continue ;
    else :
      bufls.append(l.strip()) ; 

def write_bibblines(bibdict) : 
  for key in sorted(bibdict) : 

