from readlex import latin2shaw
from zipfile import ZipFile


def main():
    with ZipFile("dune-messiah.epub") as epub_latin:
        with ZipFile("dune_messiah_out.epub", mode="w") as epub_shaw:
            for filename in epub_latin.namelist():
                print(filename)
                # text_latin = epub_latin.read(filename).decode()
                in_bytes = epub_latin.read(filename)

                if filename.endswith(".xhtml"):
                    text_latin = in_bytes.decode()
                    epub_shaw.writestr(filename, latin2shaw(text_latin, is_xml=True))
                else:
                    epub_shaw.writestr(filename, in_bytes)
