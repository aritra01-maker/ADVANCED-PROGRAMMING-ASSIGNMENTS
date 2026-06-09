# =========================================================
# File Name : score_processor.py
# Purpose   : Read a score from a file,
#             multiply it by 10,
#             and handle exceptions properly.
# =========================================================


# ---------------------------------------------------------
# Creating a class named ScoreProcessor
# ---------------------------------------------------------
class ScoreProcessor:

    # -----------------------------------------------------
    # Method : process_score_file
    #
    # Parameter:
    #   file_path -> path of the text file
    #
    # Returns:
    #   Integer result after multiplication
    # -----------------------------------------------------
    def process_score_file(self, file_path: str) -> int:

        # -------------------------------------------------
        # try block:
        # Code that may generate exceptions
        # -------------------------------------------------
        try:

            # ---------------------------------------------
            # Open file in read mode
            #
            # "with" automatically closes the file
            # after use.
            # ---------------------------------------------
            with open(file_path, "r") as file:

                # -----------------------------------------
                # Read data from file
                # -----------------------------------------
                score_text = file.read()

                # -----------------------------------------
                # Remove extra spaces/newline characters
                # -----------------------------------------
                score_text = score_text.strip()

                # -----------------------------------------
                # Convert text into integer
                #
                # Possible Error:
                # ValueError if data is not numeric
                # -----------------------------------------
                score = int(score_text)

                # -----------------------------------------
                # Multiply score by 10
                # -----------------------------------------
                result = score * 10

        # -------------------------------------------------
        # Handles missing file error
        # -------------------------------------------------
        except FileNotFoundError:

            print("Error: File not found.")

            # Re-raise exception for pytest
            raise

        # -------------------------------------------------
        # Handles invalid integer conversion
        # -------------------------------------------------
        except ValueError:

            print("Error: Invalid number format in file.")

            # Re-raise exception for pytest
            raise

        # -------------------------------------------------
        # Executes ONLY if no exception occurred
        # -------------------------------------------------
        else:

            print("Data processed successfully")

            return result

        # -------------------------------------------------
        # Executes ALWAYS
        # -------------------------------------------------
        finally:

            print("File cleanup completed")


# =========================================================
# Main Section
# This code runs only when this file is executed directly
# =========================================================
if __name__ == "__main__":

    # Create object of ScoreProcessor
    processor = ScoreProcessor()

    # Call method using valid file
    final_result = processor.process_score_file("valid_score.txt")

    # Display final result
    print("Final Result =", final_result)