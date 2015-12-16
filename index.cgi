#!/usr/bin/perl

use LWP::Simple;
use XML::Simple;
use Encode qw(is_utf8);
use CGI qw(:standard);
use strict;
use Jcode;
use URI::Escape;

my $count = 1;

my $url = "http://b.hatena.ne.jp/hotentry.rss";

my $content = LWP::Simple::get($url) or &error("はてなAPIから正常に取得できませんでした。");
my $xs = new XML::Simple(forcearray => 1);
my $ref = $xs->XMLin($content);
my @item = (ref $ref->{item} eq "ARRAY") ? @{$ref->{item}} : $ref->{item};

my($tag1, $tag2, $tag3, $tag4, $tag5, $tag6, $tag7, $tag8, $tag9);
foreach(@item){
  my $title = $_->{title}->[0];
  my $link = $_->{link}->[0];
  my $description = $_->{description}->[0];
  if(ref($description) eq "HASH"){
    $description = "";
  }
  #my $description = $_->{'content:encoded'}->[0];
  my $subject = $_->{'dc:subject'}->[0];

  my $date = $_->{'dc:date'}->[0];
  $date = substr($date, 0, 10) . " " . substr($date, 11, 5);
  $date =~ s/-/\//g;
  $date = "<span class=\"glyphicon glyphicon-time\"></span> " . $date;

  # ドメインを抽出する
  my $domain;
  if($link =~m|//(.+?)/|){
    $domain = $1;
  }else{
    $domain = "More Info";
  }

  my $bookmarkcount = $_->{'hatena:bookmarkcount'}->[0];
  if($bookmarkcount > 500){
    $bookmarkcount = "<span class=\"text-danger\"><i class=\"fa fa-fire\"></i> " . " " . $bookmarkcount . " USERS<span class=\"glyphicon glyphicon-bookmark pull-right\"></span></span>";
  }elsif($bookmarkcount > 300){
    $bookmarkcount = "<span class=\"text-warning\"><span class=\"glyphicon glyphicon-user\"></span> " . " " . $bookmarkcount . " USERS<span class=\"glyphicon glyphicon-bookmark pull-right\"></span></span>";
  }elsif($bookmarkcount > 100){
    $bookmarkcount = "<span class=\"text-success\"><span class=\"glyphicon glyphicon-user\"></span> " . " " . $bookmarkcount . " USERS<span class=\"glyphicon glyphicon-bookmark pull-right\"></span></span>";
  }else{
    $bookmarkcount = "<span class=\"text-muted\"><span class=\"glyphicon glyphicon-user\"></span> " . " " . $bookmarkcount . " USERS<span class=\"glyphicon glyphicon-bookmark pull-right\"></span></span>";
  }

  #my $tweet = $title . " " . $link;
  #$tweet = uri_escape($tweet);

  if($count == 1){
    $tag1 = <<EOT;
    <p class="bs-component">
    <a href="http://b.hatena.ne.jp/entry/$link" class="btn btn-default btn-lg btn-block" target="_blank">$bookmarkcount</a>
    </p>
    <h1><a href="$link" target="_blank">$title</a></h1>
    <p class="lead">$description</p>
    <p><span class="label label-primary">$subject</span> $date</p>
    <a class="btn btn-social-icon btn-twitter" href="http://twitter.com/share?url=$link&text=$title" target="_blank"><span class="fa fa-twitter"></span></a> <a class="btn btn-default" href="$link" target="_blank">$domain</a>
EOT
  }elsif($count == 2){
    $tag2 = <<EOT;
    <p class="bs-component">
    <a href="http://b.hatena.ne.jp/entry/$link" class="btn btn-default btn-lg btn-block" target="_blank">$bookmarkcount</a>
    </p>
    <h2><a href="$link" target="_blank">$title</a></h2>
    <p>$description</p>
    <p><span class="label label-primary">$subject</span> $date</p>
    <a class="btn btn-social-icon btn-twitter" href="http://twitter.com/share?url=$link&text=$title" target="_blank"><span class="fa fa-twitter"></span></a> <a class="btn btn-default" href="$link" target="_blank">$domain</a>
EOT
  }elsif($count == 3){
    $tag3 = <<EOT;
    <p class="bs-component">
    <a href="http://b.hatena.ne.jp/entry/$link" class="btn btn-default btn-lg btn-block" target="_blank">$bookmarkcount</a>
    </p>
    <h2><a href="$link" target="_blank">$title</a></h2>
    <p>$description</p>
    <p><span class="label label-primary">$subject</span> $date</p>
    <a class="btn btn-social-icon btn-twitter" href="http://twitter.com/share?url=$link&text=$title" target="_blank"><span class="fa fa-twitter"></span></a> <a class="btn btn-default" href="$link" target="_blank">$domain</a>
EOT
  }elsif($count == 4){
    $tag4 = <<EOT;
    <p class="bs-component">
    <a href="http://b.hatena.ne.jp/entry/$link" class="btn btn-default btn-lg btn-block" target="_blank">$bookmarkcount</a>
    </p>
    <h3><a href="$link" target="_blank">$title</a></h3>
    <p>$description</p>
    <p><span class="label label-primary">$subject</span> $date</p>
    <a class="btn btn-social-icon btn-twitter" href="http://twitter.com/share?url=$link&text=$title" target="_blank"><span class="fa fa-twitter"></span></a> <a class="btn btn-default" href="$link" target="_blank">$domain</a>
EOT
  }elsif($count == 5){
    $tag5 = <<EOT;
    <p class="bs-component">
    <a href="http://b.hatena.ne.jp/entry/$link" class="btn btn-default btn-lg btn-block" target="_blank">$bookmarkcount</a>
    </p>
    <h3><a href="$link" target="_blank">$title</a></h3>
    <p>$description</p>
    <p><span class="label label-primary">$subject</span> $date</p>
    <a class="btn btn-social-icon btn-twitter" href="http://twitter.com/share?url=$link&text=$title" target="_blank"><span class="fa fa-twitter"></span></a> <a class="btn btn-default" href="$link" target="_blank">$domain</a>
EOT
  }elsif($count == 6){
    $tag6 = <<EOT;
    <p class="bs-component">
    <a href="http://b.hatena.ne.jp/entry/$link" class="btn btn-default btn-lg btn-block" target="_blank">$bookmarkcount</a>
    </p>
    <h3><a href="$link" target="_blank">$title</a></h3>
    <p>$description</p>
    <p><span class="label label-primary">$subject</span> $date</p>
    <a class="btn btn-social-icon btn-twitter" href="http://twitter.com/share?url=$link&text=$title" target="_blank"><span class="fa fa-twitter"></span></a> <a class="btn btn-default" href="$link" target="_blank">$domain</a>
EOT
  }elsif($count == 7){
    $tag7 = <<EOT;
    <p class="bs-component">
    <a href="http://b.hatena.ne.jp/entry/$link" class="btn btn-default btn-lg btn-block" target="_blank">$bookmarkcount</a>
    </p>
    <h3><a href="$link" target="_blank">$title</a></h3>
    <p>$description</p>
    <p><span class="label label-primary">$subject</span> $date</p>
    <a class="btn btn-social-icon btn-twitter" href="http://twitter.com/share?url=$link&text=$title" target="_blank"><span class="fa fa-twitter"></span></a> <a class="btn btn-default" href="$link" target="_blank">$domain</a>
EOT
  }elsif($count == 8){
    $tag8 = <<EOT;
    <p class="bs-component">
    <a href="http://b.hatena.ne.jp/entry/$link" class="btn btn-default btn-lg btn-block" target="_blank">$bookmarkcount</a>
    </p>
    <h3><a href="$link" target="_blank">$title</a></h3>
    <p>$description</p>
    <p><span class="label label-primary">$subject</span> $date</p>
    <a class="btn btn-social-icon btn-twitter" href="http://twitter.com/share?url=$link&text=$title" target="_blank"><span class="fa fa-twitter"></span></a> <a class="btn btn-default" href="$link" target="_blank">$domain</a>
EOT
  }elsif($count == 9){
    $tag9 = <<EOT;
    <p class="bs-component">
    <a href="http://b.hatena.ne.jp/entry/$link" class="btn btn-default btn-lg btn-block" target="_blank">$bookmarkcount</a>
    </p>
    <h3><a href="$link" target="_blank">$title</a></h3>
    <p>$description</p>
    <p><span class="label label-primary">$subject</span> $date</p>
    <a class="btn btn-social-icon btn-twitter" href="http://twitter.com/share?url=$link&text=$title" target="_blank"><span class="fa fa-twitter"></span></a> <a class="btn btn-default" href="$link" target="_blank">$domain</a>
EOT
  }else{
    last;
  }

  $count++;
}

my $html = <<HTML;
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="はてなブックマークのホットエントリーの被ブックマーク数を毎日集計しています。被ブックマーク数の多かった記事を年度別、月別、日別にまとめて読むことができるWebサービスです。2015年8月から集計しています。" />
  <meta name="keywords" content="被ブックマーク数,ランキング,ホットエントリー,はてな" />
  <title>はてなブックマーク件数の集計サイト - 人気エントリーが日別・月別・年別にわかります！</title>
  <link rel="shortcut icon" href="favicon.ico">
  <link rel="stylesheet" type="text/css" href="./css/bootstrap.min.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
  <link rel="stylesheet" type="text/css" href="./css/social-buttons.css">
  <style type="text/css">
  body { padding-top: 80px; }
  \@media ( min-width: 768px ) {
    #banner {
      min-height: 300px;
      border-bottom: none;
    }
    .bs-docs-section {
      margin-top: 8em;
    }
    .bs-component {
      position: relative;
    }
    .bs-component .modal {
      position: relative;
      top: auto;
      right: auto;
      left: auto;
      bottom: auto;
      z-index: 1;
      display: block;
    }
    .bs-component .modal-dialog {
      width: 90%;
    }
    .bs-component .popover {
      position: relative;
      display: inline-block;
      width: 220px;
      margin: 20px;
    }
    .nav-tabs {
      margin-bottom: 15px;
    }
  }
  </style>

  <!--[if lt IE 9]>
    <script src="//oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="//oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->

</head>
<body>

<header>
<div class="navbar navbar-default navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
    <a href="./" class="navbar-brand"><i class="fa fa-bookmark-o"></i> はてなブックマーク</a>
    <button class="navbar-toggle" type="button" data-toggle="collapse" data-target="#navbar-main">
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>
    </div>
    <div class="navbar-collapse collapse" id="navbar-main">
    <ul class="nav navbar-nav">
      <li class="active"><a href="./"><span class="glyphicon glyphicon-home"></span> Top</a></li>
    </ul>
    </div>
  </div>
</div>
</header>

<div class="container">

    <div class="row">
      <div class="col-lg-12">
        <h1><i class="fa fa-bookmark-o"></i> はてなブックマーク</h1>
        <p class="lead">人気エントリー</p>
      </div>
    </div>

  <!-- Containers
  ================================================== -->
    <div class="row">
      <div class="col-lg-12">
        <div class="well">
          $tag1
        </div>
      </div>
    </div>

    <!-- Content Row -->
    <div class="row">

      <div class="col-md-6">
        <div class="well">
        $tag2
        </div>
      </div>
      <!-- /.col-md-6 -->

      <div class="col-md-6">
        <div class="well">
        $tag3
        </div>
      </div>
      <!-- /.col-md-6 -->

    </div>
    <!-- /.row -->

    <!-- Content Row -->
    <div class="row">

      <div class="col-md-4">
        <div class="well">
        $tag4
        </div>
      </div>
      <!-- /.col-md-4 -->

      <div class="col-md-4">
        <div class="well">
        $tag5
        </div>
      </div>
      <!-- /.col-md-4 -->

      <div class="col-md-4">
        <div class="well">
        $tag6
        </div>
      </div>
      <!-- /.col-md-4 -->

    </div>
    <!-- /.row -->

    <!-- Content Row -->
    <div class="row">

      <div class="col-md-4">
        <div class="well">
        $tag7
        </div>
      </div>
      <!-- /.col-md-4 -->

      <div class="col-md-4">
        <div class="well">
        $tag8
        </div>
      </div>
      <!-- /.col-md-4 -->

      <div class="col-md-4">
        <div class="well">
        $tag9
        </div>
      </div>
      <!-- /.col-md-4 -->

    </div>
    <!-- /.row -->

<hr>

<footer class="footer">

  <p>
  Designed and built with all the love in the world by <a href="http://tsukuba42195.top/">向井聡</a> Akira Mukai.
  </p>

</footer>
<!-- /footer -->


</div>


<script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="./js/bootstrap.min.js"></script>

<script type="text/javascript">
\$(function(){
  \$(".dropdown").hover(
  function() {
    \$('.dropdown-menu', this).stop( true, true ).slideDown("fast");
    \$(this).toggleClass('open');
  },
  function() {
    \$('.dropdown-menu', this).stop( true, true ).slideUp("fast");
    \$(this).toggleClass('open');
  });

});
</script>

</body>
</html>
HTML

print header( -type => 'text/html',-charset => 'UTF-8');
print $html;
