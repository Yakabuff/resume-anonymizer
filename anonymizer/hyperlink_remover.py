import zipfile
import ruamel.std.zipfile as zip
import re
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML

def remove_link(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(path)
    print(document.namelist())
    xml_content = document.read('word/document.xml')
    document.close()
    xml_content = xml_content.decode('utf-8')
    xml_content = xml_content.replace("</w:hyperlink>","")
    xml_content = re.sub('<w:hyperlink[^>]*>',"",xml_content)
    # print(xml_content)
    # xml_content = xml_content.encode('utf-8')
    tmpfile = open("../document.xml", "w")
    tmpfile.write(xml_content)

    # document.writestr("/document.xml", xml_content)
    zip.delete_from_zip_file(path, pattern=None, file_names='word/document.xml')
    with zipfile.ZipFile(path, 'a') as myzip:

        myzip.write('document.xml',"/word/document.xml")
        myzip.close()
    # document.write("document.xml")



# if __name__ == '__main__':
#     remove_link("test1.zip")