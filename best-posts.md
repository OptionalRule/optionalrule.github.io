---
layout: page
title: "Best Posts"
subtitle: My picks for the bests posts on the site
permalink: /best-posts/
---
<div class="row">
  <div class="col">

{% assign best_posts = site.data.best_posts %}
{% for post_filename in best_posts %}
  {% assign post_path = site.source | append: "/_posts/" | append: post_filename %}
  {% assign post = site.posts | where_exp: "post", "post.path contains post_filename" | first %}

  {% if post %}
    {% include post_preview.html %}
  {% endif %}
{% endfor %}

  </div>

  <!-- sidebar -->
  <div class="col-lg-3">

    <div class="list-group list-group-flush my-2">
      <h2 class="widget-title list-group-item">Site Search</h2>
      {% include googlesearch.html %}
    </div>

    <div class="list-group list-group-flush my-2">
      <h2 class="widget-title list-group-item">Categories</h2>
      {% for item in site.data.categories_nav %}
      <a href="{{ item.link }}" class="list-group-item list-group-item-action {% if page.url contains item.link %} active{% endif %}">
        {{ item.name }}
      </a>
      {% endfor %}
    </div>

    <div class="list-group list-group-flush my-2">
      <h2 class="widget-title list-group-item">Socials</h2>
      {% for item in site.data.socials %}
      <a rel="me" href="{{ item.link }}" target="_blank" class="list-group-item list-group-item-action" rel="noopener">
        <i class="fab fa-{{ item.name }}"></i>
        {{ item.title }}
      </a>
      {% endfor %}
    </div>

    <div class="list-group list-group-flush my-2">
      <h2 class="widget-title list-group-item">Gaming Blogs</h2>
      {% for item in site.data.blogroll %}
      <a href="{{ item.link }}" target="_blank" class="list-group-item list-group-item-action" rel="noopener">{{ item.name }}</a>
      {% endfor %}
    </div>

  </div>
</div>