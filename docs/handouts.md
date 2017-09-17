---
layout : page
title  : Handouts
permalink : handouts
---

# 2016-2017

{% for handout in site.handouts %}
    {% if handout.category == "2016-2017" %}
- [{{handout.title}}]({{ handout.url | prepend: site.baseurl }})
    {% endif %}
{% endfor %}
