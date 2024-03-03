# -*- coding: utf-8 -*-

from learn_pyside6.paths import dir_doc_source
from learn_pyside6.rename_sequencially import rename_sequentially

for dir_root in dir_doc_source.select_dir(
    recursive=False,
    filters=lambda p: p.basename != "_static",
):
    rename_sequentially(dir_root=dir_root)
