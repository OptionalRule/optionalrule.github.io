---
layout: page
title: "Most Popular Posts"
permalink: /popular-posts/
---

{% assign view_counts = site.data.view_counts %}
{% assign popular_posts = site.posts | sort: 'date' | reverse %}

{% assign posts_with_views = '' | split: '' %}
{% for post in popular_posts %}
  {% assign post_url = post.url | relative_url %}
  {% assign post_url_alt = post_url | remove_first: '/' %}
  {% assign view_count = view_counts[post_url] | default: view_counts[post_url_alt] | default: 0 %}
  {% assign post_with_views = view_count | append: ',' | append: post.url %}
  {% assign posts_with_views = posts_with_views | push: post_with_views %}
{% endfor %}

{% assign sorted_posts = posts_with_views | sort | reverse %}

<div class="row">
  <div class="col">
    {% for post_info in sorted_posts limit:25 %}
        {% assign post_data = post_info | split: ',' %}
        {% assign view_count = post_data[0] %}
        {% assign post_url = post_data[1] %}
        {% assign post = site.posts | where: "url", post_url | first %}
        {% include post_preview.html %}
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