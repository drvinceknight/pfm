---
layout : default
title  : Computing for Mathematics
---

This is the course page for the Computing for Mathematics course taught at the
School of Mathematics at Cardiff University.

# Lab Sheets

{% for sheet in site.labsheets %}
- [{{sheet.title}}]({{ sheet.url | prepend: site.baseurl }})
{% endfor %}

# Handouts

{% for handout in site.handouts %}
    {% if handout.categories contains "2017-2018" %}
- [{{handout.title}}]({{ handout.url | prepend: site.baseurl }})
    {% endif %}
{% endfor %}

# Assessment

{% for assessment in site.assessment %}
- [{{assessment.title}}]({{ assessment.url | prepend: site.baseurl }})
{% endfor %}


# Help

- [Chat room](https://gitter.im/computing-for-mathematics/Lobby).
- There are discussion boards on each lab sheet.
- Email me: `knightva@cardiff.ac.uk`.
- My office hours: Thursday 1300-1500.
