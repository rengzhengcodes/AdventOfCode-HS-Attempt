for i in {1..25};
	do mkdir Day$i
	touch Day$i/input.txt
	touch Day$i/ex.txt
	pytemplate="`cat template.py`"
	echo "$pytemplate" >> Day$i/Advent$i.py
	javaraw="`cat template.java`"
	javatemplate=${javaraw/template/Advent$i}
	echo "$javatemplate" >>  Day$i/Advent$i.java
done
