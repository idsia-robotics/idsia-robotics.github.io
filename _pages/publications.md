---
layout: splash
author_profile: false
classes: wide
title: "Publications"
permalink: /publications/
---

# Publications

## Full list

<div class="bibtex_display">
{% assign pubs_by_year = site.data.publications | group_by: "year" %}
{% assign sorted_groups = pubs_by_year | sort: "name" | reverse %}

{% for group in sorted_groups %}
<h2 class="year" id="year-{{ group.name }}">{{ group.name | default: "Other Publications" }}</h2>

{% for pub in group.items %}
<div class="bibtex_entry_full bibtexentry">

  <span class="title">{{ pub.title }}</span>.
  {% if pub.authors_display %}<span class="author">{{ pub.authors_display }}</span>.{% endif %}
  {% if pub.journal %}
    <em>{{ pub.journal }}</em>{% if pub.volume %}, vol. {{ pub.volume }}{% endif %}{% if pub.number %}, no. {{ pub.number }}{% endif %},
  {% elsif pub.booktitle %}
    In <em>{{ pub.booktitle }}</em>,
  {% endif %}
  {% if pub.pages %}pp. {{ pub.pages }},{% endif %}
  {{ pub.year }}.
  {% if pub.note %}<span style="font-weight: bold;">({{ pub.note }})</span>{% endif %}
  {% if pub.special_note %}<span style="font-weight: bold;">({{ pub.special_note }})</span>{% endif %}
  {% if pub.url %}<a href="{{ pub.url }}" title="view online"><i class="fas fa-search"></i></a>{% endif %}
  {% if pub.file %}<a href="{{ pub.file }}" title="download pdf"><i class="fas fa-file"></i></a>{% endif %}
  {% if pub.website %}<a href="{{ pub.website }}" title="visit website"><i class="fas fa-globe-europe"></i></a>{% endif %}

</div>
{% endfor %}

{% endfor %}
</div>

&nbsp;
