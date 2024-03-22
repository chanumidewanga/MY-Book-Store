-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 18, 2022 at 10:50 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `abc_books_store`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `bookNo` char(5) NOT NULL,
  `title` varchar(40) NOT NULL,
  `subjectCode` varchar(6) NOT NULL,
  `author` varchar(20) NOT NULL,
  `publisher` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `location` varchar(20) NOT NULL,
  `edition` int(2) NOT NULL,
  `chapters_count` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`bookNo`, `title`, `subjectCode`, `author`, `publisher`, `price`, `location`, `edition`, `chapters_count`) VALUES
('22001', 'Harry Potter and the Half-Blood Prince', 'FAN', 'J.K. Rowling', 'Bloomsbury', 5680, 'A001', 3, 5),
('22002', 'The Hunger Games', 'ADV', 'Suzanne Collins', 'Scholastic Press', 7500, 'A001', 1, 4),
('22003', 'The Lightning Thief', 'FAN', 'Rick Riordan', 'Miramax Books', 1195, 'A002', 5, 4),
('22004', 'Little Women', 'CLA', 'Louisa May Alcott', 'Robert Brothers', 1764, 'D001', 1, 3),
('22005', 'Dune', 'SCI', 'Frank Herbert', 'Chilton Books', 4000, 'S008', 1, 5);

-- --------------------------------------------------------

--
-- Table structure for table `book_chapter`
--

CREATE TABLE `book_chapter` (
  `bookNo` char(5) NOT NULL,
  `chapterNo` int(4) NOT NULL,
  `chapter_title` varchar(25) NOT NULL,
  `starting_page_No` int(4) NOT NULL,
  `ending_page_No` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book_chapter`
--

INSERT INTO `book_chapter` (`bookNo`, `chapterNo`, `chapter_title`, `starting_page_No`, `ending_page_No`) VALUES
('22001', 1, 'The Other Minister', 4, 25),
('22001', 2, 'Spinner\'s End', 26, 51),
('22001', 3, 'Will and Won\'t', 52, 70),
('22001', 4, 'Horace Slughorn', 71, 94),
('22002', 1, 'Chapter 1', 6, 31),
('22002', 2, 'Chapter 2', 32, 68),
('22002', 3, 'Chapter 3', 69, 110),
('22002', 4, 'Chapter 4', 110, 151),
('22003', 1, 'My Pre-algebra Teacher', 3, 28),
('22003', 2, 'Three Old Ladies', 29, 56),
('22003', 3, 'We capture a flag', 57, 75),
('22003', 4, 'I am Offered a Quest', 76, 92),
('22004', 1, 'Playing Pilgrims', 6, 10),
('22004', 2, 'A Merry Christmas', 11, 26),
('22004', 3, 'The Laurence Boy', 27, 39),
('22005', 1, 'CHAPTER ONE DUNE', 13, 45),
('22005', 2, 'CHAPTER TWO DUNE', 46, 70),
('22001', 5, 'An Excess of Phlegm', 95, 126),
('22005', 3, 'CHAPTER THREE DUNE', 47, 78),
('22005', 4, 'CHAPTER FOUR DUNE', 79, 92),
('22005', 5, 'CHAPTER FIVE DUNE', 93, 150);

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `subject_code` char(5) NOT NULL,
  `name` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`subject_code`, `name`) VALUES
('ADV', 'adventure'),
('CLA', 'classic'),
('COM', 'comic'),
('FAN', 'fantasy'),
('HIS', 'history'),
('KID', 'kids'),
('LIT', 'literary'),
('NOV', 'novel'),
('POE', 'poetry'),
('SCI', 'science fiction'),
('THR', 'thriller');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`bookNo`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`subject_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
