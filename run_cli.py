#!/usr/bin/env python3
"""
Script de lancement pour la version CLI
"""

import sys
import os

# Ajoute le répertoire parent au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from cli.main import main

if __name__ == '__main__':
    main()