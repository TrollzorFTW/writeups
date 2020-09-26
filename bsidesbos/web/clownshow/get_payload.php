<?php
      $name = 'ntj'; // enter any name
      $answer = 'qweqweasda'; // enter at least a 10 character  answer
      $time = 1000000000; // enter at least a 10 digit time to get pass that first if statement
      $digits = strlen(strval($time));
      $good_answer = '0';
 
      while(true){ 
	if (is_numeric($time) && $digits >= 10) {
            $key = hash('sha256', $name . $answer . $time);
          //  echo $key;
	} 

        else {
            $key = hash('sha256',$name . $answer . time());
        } 
	$result = substr($key,5,25);
	if($result == $good_answer){
		echo "[!] Found the time: ".$time.PHP_EOL;
		echo "[!] Payload: name=".$name."&answer=".$answer."&time=".$time.PHP_EOL;
		die;
		}
	else{
		$time = $time + 1;
	}
	}
?>
