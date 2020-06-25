<h1 align="center"> Python-project-lvl2 </h1>

<div align="center">
	<a href="https://travis-ci.com/aldangold/python-project-lvl2">
		<img src="https://travis-ci.com/aldangold/python-project-lvl2.svg?branch=master" />
	</a> 
    <a href="https://codeclimate.com/github/aldangold/python-project-lvl2/maintainability">
        <img src="https://api.codeclimate.com/v1/badges/c874a3eb5668cd2e52a4/maintainability" />
	</a>
	<a href="https://codeclimate.com/github/aldangold/python-project-lvl2/test_coverage">
		<img src="https://api.codeclimate.com/v1/badges/c874a3eb5668cd2e52a4/test_coverage" />
	</a>
</div>

<h2>:performing_arts: Gen difference is an application that helps you find the difference. </h2>
	<p>This project is a console application that allows you to merge two files for changes. Supported file types are Json and Ymal. The format of the result of the changes is displayed on the screen and is available in the Json, Plain Text and Classic Cascading formats.</p>

<h2>:package: Installation Guide </h2>
		<ul>
		  	<li> 
		  	<p>Install Python dependencies - pyyaml </p>
		  	</li>
		  	<pre>$pip install pyyaml</pre>
			<li> <p>Install aldangold-gendiff</p>
		  	</li>
		  	<pre>$pip install --index-url https://test.pypi.org/simple aldangold-gendiff</pre>
			<li> <p>Call context help</p>
		  	</li>
		  	<pre>$gendiff -h</pre>
		</ul>
		<p align="center">
			<a href="https://asciinema.org/a/opzEEFAqiw2EmsbC0EX2bvsHP" target="_blank">
			<img src="https://asciinema.org/a/opzEEFAqiw2EmsbC0EX2bvsHP.svg" width="80%"/></a>
		</p>

<h2> :rocket: Launch and demo of gendiff</h2>
<h4> Demonstration of output of comparison results two flat files type of JSON in cascade format.</h4>
    <p>before.json</p>
		<pre>
{
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22"
  }
  		</pre>
  	<p>after.json</p>
	  	<pre>
{
    "timeout": 20,
    "verbose": true,
    "host": "hexlet.io"
  }
  	</pre>
	<pre>$gendiff -f cascade before.json after.json</pre>
		<p align="center">
			<a href="https://asciinema.org/a/EUNVV1iHwlBMichJkjcisxD3r" target="_blank">
			<img src="https://asciinema.org/a/EUNVV1iHwlBMichJkjcisxD3r.svg" width="80%" /></a>
		</p>
<h4> Demonstration of output of comparison results two flat files type of YAML in cascade format.</h4>
	<pre>$gendiff -f cascade before.yml after.yml</pre>
		<p align="center">
			<a href="https://asciinema.org/a/1FR0IBlUWs3Fb4pfyo3VkmD7n" target="_blank">
			<img src="https://asciinema.org/a/1FR0IBlUWs3Fb4pfyo3VkmD7n.svg" width="80%" /></a>
		</p>
<h4> Demonstration of the results of comparing two files of a nested structure in accessible formats.	</h4>
	<p>before.json</p>
		<pre>
{
  "common": {
    "setting1": "Value 1",
    "setting2": "200",
    "setting3": true,
    "setting6": {
      "key": "value"
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar"
  },
  "group2": {
    "abc": "12345"
  }
}
  		</pre>
  	<p>after.json</p>
	<pre>
{
  "common": {
    "setting1": "Value 1",
    "setting3": true,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    }
  },

  "group1": {
    "foo": "bar",
    "baz": "bars"
  },

  "group3": {
    "fee": "100500"
  }
}
  	</pre>
	<h4> Demonstration of the output of the difference in the default format - plain text.</h4>
	<pre>$gendiff before.json after.json</pre>
		<p align="center">
			<a href="https://asciinema.org/a/q1pFiRmmljMJ01bJZBbgB9jdt" target="_blank">
			<img src="https://asciinema.org/a/q1pFiRmmljMJ01bJZBbgB9jdt.svg" width="80%"/></a>
		</p>
	<h4> Demonstration of the output of the difference in the format - cascade.</h4>
	<pre>$gendiff -f cascade before.json after.json</pre>
		<p align="center">
			<a href="https://asciinema.org/a/DL8CNXY7Ot6JGKUq4m6a3km6N" target="_blank">
			<img src="https://asciinema.org/a/DL8CNXY7Ot6JGKUq4m6a3km6N.svg" width="80%"/></a>
		</p>
	<h4> Demonstration of the output of the difference in the format - JSON.</h4>
	<pre>$gendiff -f json before.json after.json</pre>
		<p align="center">
			<a href="https://asciinema.org/a/LKj292acxYKSqDbXxH6l4ksIN" target="_blank">
			<img src="https://asciinema.org/a/LKj292acxYKSqDbXxH6l4ksIN.svg" width="80%"/></a>
		</p>