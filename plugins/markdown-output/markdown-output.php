<?php if (!defined('PmWiki')) exit();

/*	=== MarkdownOutput ===
 *	Copyright 2008 Eemeli Aro <eemeli.aro@tkk.fi>
 *
 *	Presents a wiki page in Markdown format instead of HTML
 *
 *	Based on Milian Wolff's Markdownify HTML to Markdown converter,
 *	available from <http://milianw.de/projects/markdownify/> and
 *	licensed under the LGPL.
 *
 *	To install, add the following line to your config file :
	include_once("$FarmD/cookbook/markdown-output/markdown-output.php");
 *
 *	For more information, please see the online documentation at
 *		http://www.pmwiki.org/wiki/Cookbook/MarkdownOutput
 *
 *	This program is free software; you can redistribute it and/or
 *	modify it under the terms of the GNU General Public License as
 *	published by the Free Software Foundation; either version 2 of
 *	the License, or (at your option) any later version.
 */

$RecipeInfo['MarkdownOutput']['Version'] = '2008-02-15-2';

$HandleActions['markdown'] = 'HandleMarkdownOutput';

if ($action=='markdown') require_once dirname(__FILE__).'/markdownify/markdownify_extra.php';

function HandleMarkdownOutput( $pagename, $auth = 'read' ) {
	global $DefaultPageTextFmt, $PageNotFoundHeaderFmt, $HTTPHeaders, $TmplDisplay,
	$MarkdownExtra, $MarkdownLinksAfterEachParagraph, $MarkdownBodyWidth, $MarkdownKeepHTML;
	$page = RetrieveAuthPage( $pagename, $auth, true, READPAGE_CURRENT );
	if (!$page) Abort("?cannot markdown $pagename");
	PCache($pagename,$page);
	if ( PageExists($pagename) ) $text = @$page['text'];
	else {
		SDV($DefaultPageTextFmt, '(:include $[{$SiteGroup}.PageNotFound]:)' );
		$text = FmtPageName( $DefaultPageTextFmt, $pagename );
		SDV($PageNotFoundHeaderFmt, 'HTTP/1.1 404 Not Found' );
		SDV($HTTPHeaders['status'], $PageNotFoundHeaderFmt );
	}
	$text = '(:groupheader:)'.@$text.'(:groupfooter:)';
	$html = MarkupToHTML( $pagename, $text );

	if ( empty($TmplDisplay['PageTitleFmt']) ) $html = "<h1>".PageVar($pagename,'$Title')."</h1>\n".$html;

	foreach ($HTTPHeaders as $h) {
		$h = preg_replace( '!^Content-type:\\s+text/html!i', 'Content-type: text/plain', $h );
		header($h);
	}

	SDV($MarkdownLinksAfterEachParagraph, FALSE );
	SDV($MarkdownBodyWidth, FALSE );
	SDV($MarkdownKeepHTML, FALSE );
	$mdf = IsEnabled($MarkdownExtra,TRUE) ? 'Markdownify_Extra' : 'Markdownify';
	$md = new $mdf( $MarkdownLinksAfterEachParagraph, $MarkdownBodyWidth, $MarkdownKeepHTML );
	echo $md->parseString($html);
}

