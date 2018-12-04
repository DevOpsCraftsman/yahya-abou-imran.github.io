cv_odt='CV-Alexandre-Poitevin-fr.odt'
cv_pdf='CV-Alexandre-Poitevin-fr.pdf'
cv_md='README.md'
cv_docx='CV-Alexandre-Poitevin-fr.docx'
makecv:
	libreoffice --convert-to pdf $(cv_odt)
	pandoc -o $(cv_docx) $(cv_odt)
	pandoc $(cv_odt) -t markdown | sed 's/\[\]{\#anchor}//' | sed 's/>\\/>/' > $(cv_md)
