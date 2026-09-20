#!/usr/bin/env python3
"""Wrapper du parc perso autour de l'outil pro ~/code/tools/pbn-legal.

L'outil pro a son ROOT code en dur sur `~/code/sites/blogs-geo`, la flotte
datashake. On ne le modifie pas : on surcharge ROOT avant l'appel, pour que les
pages soient ecrites dans le parc perso. Meme methode que pour brunch-story et
mamie-the le 2026-09-12.
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/code/tools/pbn-legal"))
import pbn_legal

pbn_legal.ROOT = os.path.expanduser("~/code/sites/pbn-perso")
if __name__ == "__main__":
    args = sys.argv[1:] or ["pbn-geo-gouter-gourmand"]
    sys.argv = ["pbn_legal.py"] + args
    pbn_legal.main()
