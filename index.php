<?php
$data = file("availability.log",FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES); //read the entire file to array by ignoring new lines and spaces
//DEBUG
//echo "<pre/>";print_r($data); // print output of the above line

$final_array = array(); // create an empty array
?>


<html>
<head>
  <style>
  li.green {color: green;}
  li.red {color: red;}
  </style>
</head>
<body>
<ul>


<?php
foreach ($data as $key=> $dat){ // iterate over file() generated array

    $final_data = explode('-',$dat); //explode the data with space

    //now assign the value to corresponding indexes

    $final_array[$key]['productname']  = $final_data[0];
    $final_array[$key]['asin']  = $final_data[1];
    $final_array[$key]['availability']   = $final_data[2];
    $final_array[$key]['status']   = $final_data[3];
?>

    <li class="<?php echo $final_array[$key]['status'] ?>">
      <?php echo $final_array[$key]['productname'] ?>
      http://www.amazon.de/dp/<?php echo $final_array[$key]['asin'] ?>
      <?php echo $final_array[$key]['availability'] ?>
      <?php echo $final_array[$key]['status'] ?>
<!-- //AFFILIATE LINKS -->
<?php if ($final_array[$key]['asin'] == 'B072J25TPG') { ?><iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=DE&source=ac&ref=tf_til&ad_type=product_link&tracking_id=florianmuller-21&marketplace=amazon&region=DE&placement=B072J25TPG&asins=B072J25TPG&linkId=ae50680482171845f7190af05d7e9aa5&show_border=false&link_opens_in_new_window=false&price_color=333333&title_color=0066c0&bg_color=ffffff"></iframe><?php } else {}?>
<?php if ($final_array[$key]['asin'] == 'B08B42QFNG') { ?><iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=DE&source=ac&ref=tf_til&ad_type=product_link&tracking_id=florianmuller-21&marketplace=amazon&region=DE&placement=B08B42QFNG&asins=B08B42QFNG&linkId=443494a0c3d28af219adb06a0997dc9a&show_border=false&link_opens_in_new_window=false&price_color=333333&title_color=0066C0&bg_color=FFFFFF"></iframe><?php } else {}?>
<?php if ($final_array[$key]['asin'] == 'B08B42QX93') { ?><iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=DE&source=ac&ref=tf_til&ad_type=product_link&tracking_id=florianmuller-21&marketplace=amazon&region=DE&placement=B08B42QX93&asins=B08B42QX93&linkId=f6e35a81fab303a6a3b11d2873d15ce9&show_border=false&link_opens_in_new_window=false&price_color=333333&title_color=0066c0&bg_color=ffffff"></iframe><?php } else {}?>
<?php if ($final_array[$key]['asin'] == 'B07SFHCTZ9') { ?><iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=DE&source=ac&ref=tf_til&ad_type=product_link&tracking_id=florianmuller-21&marketplace=amazon&region=DE&placement=B07SFHCTZ9&asins=B07SFHCTZ9&linkId=873805fef7f577cc440d159ca5fc770f&show_border=false&link_opens_in_new_window=false&price_color=333333&title_color=0066c0&bg_color=ffffff"></iframe><?php } else {}?>
<?php if ($final_array[$key]['asin'] == 'B087VMFKJH') { ?><iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=DE&source=ac&ref=tf_til&ad_type=product_link&tracking_id=florianmuller-21&marketplace=amazon&region=DE&placement=B087VMFKJH&asins=B087VMFKJH&linkId=dfc4a2715652a115cc1bd2f41ff57a9f&show_border=false&link_opens_in_new_window=false&price_color=333333&title_color=0066c0&bg_color=ffffff"></iframe><?php } else {}?>
<?php if ($final_array[$key]['asin'] == 'B087VMRWMC') { ?><iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=DE&source=ac&ref=tf_til&ad_type=product_link&tracking_id=florianmuller-21&marketplace=amazon&region=DE&placement=B087VMRWMC&asins=B087VMRWMC&linkId=bd9c67234e6acf8279bb3d8fd9987ad8&show_border=false&link_opens_in_new_window=false&price_color=333333&title_color=0066c0&bg_color=ffffff"></iframe><?php } else {}?>
<?php if ($final_array[$key]['asin'] == 'B08B4CFPGM') { ?><iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=DE&source=ac&ref=tf_til&ad_type=product_link&tracking_id=florianmuller-21&marketplace=amazon&region=DE&placement=B08B4CFPGM&asins=B08B4CFPGM&linkId=2a7f437423b7d7f914de03a2b1d423d7&show_border=false&link_opens_in_new_window=false&price_color=333333&title_color=0066c0&bg_color=ffffff"></iframe></iframe><?php } else {}?>
<?php if ($final_array[$key]['asin'] == 'B087VHTFSG') { ?><iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=DE&source=ac&ref=tf_til&ad_type=product_link&tracking_id=florianmuller-21&marketplace=amazon&region=DE&placement=B087VHTFSG&asins=B087VHTFSG&linkId=a6660e39f5c92b3ec615a948197b9b20&show_border=false&link_opens_in_new_window=false&price_color=333333&title_color=0066c0&bg_color=ffffff"></iframe></iframe><?php } else {}?>
    </li>

<?php
}
//DEBUG
//echo "<pre/>";print_r($final_array); // print the final output
?>

</ul>
</body>
</html>
