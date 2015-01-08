---
layout: post-index
title: 聆雨亭
tagline: Supporting tagline
---
{% include JB/setup %}

{% for post in paginator.posts %}
<article class="hentry">
  <header>
    <div class="entry-meta"><span class="entry-date date published updated"><time datetime="{{ post.date | date_to_xmlschema }}"><a href="{{ site.url }}{{ post.url }}">{{ post.date | date: "%B %d, %Y" }}</a></time></span><span class="author vcard"><span class="fn"><a href="{{ site.url }}/about/" title="About {{ site.owner.name }}">{{ site.owner.name }}</a></span></span>{% if site.disqus_shortname and post.comments %}&nbsp; &bull; &nbsp;<span class="entry-comments"><a href="{{ site.url }}{{ post.url }}#disqus_thread">Comment</a></span>{% endif %}</div><!-- /.entry-meta -->
    {% if post.link %}
      <h1 class="entry-title"><a href="{{ site.url }}{{ post.url }}" rel="bookmark" title="{{ post.title }}"><i class="icon-double-angle-right"></i></a> <a href="{{ post.link }}">{{ post.title }}</a></h1>
    {% else %}
      <h1 class="entry-title"><a href="{{ site.url }}{{ post.url }}" rel="bookmark" title="{{ post.title }}" itemprop="url">{{ post.title }}</a></h1>
    {% endif %}
  </header>
  <div class="entry-content">
    {{ post.content | split:'<!--more-->' | first }}
  </div><!-- /.entry-content -->
</article><!-- /.hentry -->
{% endfor %}


{% if paginator.total_pages > 1 %}
<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path | prepend: site.baseurl | replace: '//', '/' }}">&laquo; Prev</a>
  {% else %}
    <span>&laquo; Prev</span>
  {% endif %}

  {% for page in (1..paginator.total_pages) %}
    {% if page == paginator.page %}
      <em>{{ page }}</em>
    {% elsif page == 1 %}
      <a href="{{ '/index.html' | prepend: site.baseurl | replace: '//', '/' }}">{{ page }}</a>
    {% else %}
      <a href="{{ site.paginate_path | prepend: site.baseurl | replace: '//', '/' | replace: ':num', page }}">{{ page }}</a>
    {% endif %}
  {% endfor %}

  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path | prepend: site.baseurl | replace: '//', '/' }}">Next &raquo;</a>
  {% else %}
    <span>Next &raquo;</span>
  {% endif %}
</div>
{% endif %}

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>





