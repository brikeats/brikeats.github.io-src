import os
import re
import html
from glob import glob


PAGE_NAME = 'beer'

HEADER = """Title: Beer Recipes
Slug: beer-recipes
Author: Brian Keating
Summary: Beer Recipes
save_as: %s


Recipes formulated with the help of Brewer's Friend [recipe calculator](https://www.brewersfriend.com/homebrew/recipe/calculator).

""" % (PAGE_NAME + '.html')


def parse_recipe_title(recipe_filename):
    with open(recipe_filename) as f:
        html_str = f.read()
    title_pattern = re.compile('<title.*?>(.+?)</title>')
    title = re.findall(title_pattern, html_str)[0]
    title = html.unescape(title)
    title = title.replace(' | Brewer\'s Friend', '')
    return title



if __name__ == '__main__':

    # output is a markdown file in the static page folder
    script_dir = os.path.dirname(__file__)
    static_pages_dir = os.path.join(script_dir, '..', 'pages')
    output_filename = os.path.join(static_pages_dir, PAGE_NAME + '.md')
    
    # html files in this folder are the beer recipes    
    beer_recipes = glob(os.path.join(script_dir, '*.html'))
    
    
    with open(output_filename, 'wt') as f:
        f.write(HEADER)
        for beer_recipe_fn in beer_recipes:
            beer_name = parse_recipe_title(beer_recipe_fn)
            link_url = os.path.join('beer', os.path.basename(beer_recipe_fn))
            recipe_markdown = '[%s](%s)\n' % (beer_name, link_url)
            f.write(recipe_markdown)


