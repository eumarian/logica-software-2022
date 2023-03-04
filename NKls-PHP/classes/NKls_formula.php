<?php
/*
Optional course - Logic and software - Department of Philosophy - University of Bucharest. 2022. All rights reserved, except for educational purposes. mc@filos.ro
*/
class NKls_formula{
	protected $string = '';
	protected $op = NULL;
	protected $subformula1 = NULL;
	protected $subformula2 = NULL;
	
	public function __construct($subformula1, $op = NULL, $subformula2 = NULL){
		$this->op = $op;
		$this->subformula1 = $subformula1;
		$this->subformula2 = $subformula2;
		
		if(!$op && is_object($this->subformula1)){
			$this->subformula1 = $this->subformula1->string();
		}
		
		$this->string = $this->string_create();
	}
	
	//not implemented, should validate line
	public function is_valid_formula(){
		
	}
	
	protected function string_create(){
		$ret = '';
		if($this->is_atomic()){
			$ret = $this->subformula1;
		}
		else if($this->op == '~'){
			$ret = $this->op.$this->subformula1->string(true);
		}	
		else{
			$ret = $this->subformula1->string(true).' '.$this->op.' '.$this->subformula2->string(true);
		}
		return $ret;
	}
	
	public function string($external_brackets = false){
		$ret = $this->string;
		if($external_brackets && !$this->is_atomic() && $this->op != '~'){
			$ret = '('.$ret.')';
		}
		return $ret;
	}
	
	public function is_atomic(){
		return !$this->op();
	}
	
	public function op(){
		return $this->op;
	}
	public function subformula1(){
		return $this->subformula1;
	}
	public function subformula2(){
		return $this->subformula2;
	}
	
	// array of arrays of decomposition, main to secondary, left to right
	public function subformulas(){
		$ret = array(
					0 => is_object($this->subformula1) ? $this->subformula1->subformulas() :  $this->subformula1, 
					1 => $this->op, 
					2 => is_object($this->subformula2) ? $this->subformula2->subformulas() :  $this->subformula2  );
		return $ret;
	}
	
	public function subformulas_flat($as_objects = false){
		if(!$as_objects){
			$ret = array_merge(
					array($this->string() => $this->string()),
					is_object($this->subformula1) ? $this->subformula1->subformulas_flat() :   array(),
					is_object($this->subformula2) ? $this->subformula2->subformulas_flat() :   array()
				);
		}
		else{
			$ret = array_merge(
					array($this->string() => $this),
					is_object($this->subformula1) 
							? $this->subformula1->subformulas_flat(true) 
							:  array(),
					is_object($this->subformula2) 
							? $this->subformula2->subformulas_flat(true) 
							:  array()
				);
		}
		return $ret;
	}
	
	//op no
	public function length(){
		$ret = 0;
		if(!$this->is_atomic()){
			$l1 = $this->subformula1->length();
			$l2 = $this->subformula2 ? $this->subformula2->length() : 0;
			$ret = max($l1,$l2) +1;
		}
		return $ret;
	} 	
	
	public function has_dn($recursive = true){
		return false;
	}
}

?>