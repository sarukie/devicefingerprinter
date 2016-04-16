<?php

$aData = $_REQUEST;
header('Content-Type: application/json');
echo json_encode($aData);
