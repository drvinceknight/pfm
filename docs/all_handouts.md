---
layout : page
title  : Handouts
permalink : all_handouts
---

# 2016-2017

{% for handout in site.handouts %}
    {% if handout.categories contains '2016-2017' %}
- [{{handout.title}}]({{ handout.url | prepend: site.baseurl }})
    {% endif %}
{% endfor %}
