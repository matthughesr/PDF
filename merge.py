from PyPDF2 import PdfMerger

merger = PdfMerger()
pdfs = ['Sprint 2 Documents (10).pdf', 'Sprint 2 Documents (1).pdf', 'Sprint 2 Documents (2).pdf', 'Sprint 2 Documents (3).pdf', 'Sprint 2 Documents (4).pdf', 'Sprint 2 Documents (5).pdf', 'Sprint 2 Documents (6).pdf', 'Sprint 2 Documents (7).pdf', 'Sprint 2 Documents (8).pdf', 'Sprint 2 Documents (9).pdf', 'Sprint2Wireframes.pdf']

for pdf in pdfs:
    merger.append(pdf)

merger.write("Sprint2Documents.pdf")
merger.close()
