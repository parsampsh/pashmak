<?php

function run_code($code, $stdin){
    /* Run code */

    // write code to a temp file
    $tmp_path = '/tmp/temp-script-' . time() . rand() . '.pashm';
    $tmp_path_stdin = $tmp_path . '.stdin';
    $f = fopen($tmp_path, 'w');
    fwrite($f, $code);
    fclose($f);

    // write recived stdin to tempfile
    $f = fopen($tmp_path_stdin, 'w');
    fwrite($f, $stdin);
    fclose($f);

    // run code with `runner` user and put output to temp file
    $cmd = 'cat ' . $tmp_path_stdin . ' | timeout 20s /bin/pashmak ' . $tmp_path;
    system($cmd);

    // remove temp files
    unlink($tmp_path);
    unlink($tmp_path_stdin);
}

// check form submited
$code = '';
$stdin = '';
if($_SERVER['REQUEST_METHOD'] === 'POST'){
    $code = $_POST['code'];
    $stdin = $_POST['stdin'];
}

// if any code submited, run this and show output
ob_start();
$output = null;
if($code !== ''){
    run_code($code, $stdin);
}
$output = ob_get_clean();

// show view
include 'view.php';
