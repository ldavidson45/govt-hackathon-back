from docx import Document


def parse_document(document):

    doc = Document(document)

    max_search = 30

    document_find = ['Description', "CONTRACTOR PERSONNEL", "General",
                    "Combined Synops", "Line items", "GOVERN", "Applicable",
                    "RESPONSES", "PURPOSE", "BACKGROUND", "PWS"]

    Default = "No relevant information found"


    main_dictionary = {}
    for i in range(len(doc.paragraphs)):
        for x in range(len(document_find)):
            if document_find[x] in doc.paragraphs[i].text[:max_search]:
                main_dictionary[document_find[x]] = doc.paragraphs[i].text
                count = 0
                test = 0

    return main_dictionary