����   A \  java1/student  java/lang/Object Name Ljava/lang/String; Roll_number I <init> ()V Code
   	 
 LineNumberTable LocalVariableTable this Ljava1/student; studentDetails	    java/lang/System   out Ljava/io/PrintStream;	          makeConcatWithConstants &(Ljava/lang/String;)Ljava/lang/String;
   " ! java/io/PrintStream # $ println (Ljava/lang/String;)V	  &    (  ) (I)Ljava/lang/String; main ([Ljava/lang/String;)V - java/util/Scanner	  / 0 1 in Ljava/io/InputStream;
 , 3 	 4 (Ljava/io/InputStream;)V
   7 Enter name:
 , 9 : ; nextLine ()Ljava/lang/String; = Enter roll number:
 , ? @ A nextInt ()I
  C  
 args [Ljava/lang/String; sc Ljava/util/Scanner; std 
SourceFile student.java BootstrapMethods
 M O N $java/lang/invoke/StringConcatFactory  P �(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite; L S Name: U Roll number: InnerClasses X %java/lang/invoke/MethodHandles$Lookup Z java/lang/invoke/MethodHandles Lookup !                    	 
     /     *� �                          
     Q     � *� �   � � *� %� '  � �               	             	 * +     �     8� ,Y� .� 2L� Y� 5M� 6� ,+� 8� � <� ,+� >� %,� B�       "           #  +  3  7          8 D E    - F G   % H    I    J K     Q  R Q  T V   
  W Y [ 