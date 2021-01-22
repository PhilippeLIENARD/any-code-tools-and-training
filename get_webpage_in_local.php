<?php
/*
declare a function who gets the content of a webpage and pass $url in argument 

AND

replace all occurances

AND

write the result in local
-----------------------
use Curl

int curl in a curl handling var

set options :
curl_setopt(SESSION , CURLOPT_*** , value)

*** is :

    URL
    RETURNTRANSNFERT
    CONNECTTIMEOUT
    

$data = start session curl_exec()

curl_close()

$data = str_replace(what_find , replace_by , where)

function getWebPage($url, $what_find , $replace_by){

    $ch = curl_init;

    $timeout = 5;

    curl_setopt($ch  , CURLOPT_URL , $url);
    curl_setopt($ch  , CURLOPT_RETURNTRANSNFERT , 1);
    curl_setopt($ch  , CURLOPT_CONNECTTIMEOUT , $timeout);

    $data = curl_exec();

    curl_close(); 

    $data = str_replace($what_find , $replace_by , $data);

    file_input_contents( 'localcopyfile.html' , $data);

}

getWebPage('http', 'get' , 'put');