import java.util.*;

// ---------------- BASE CLASS ----------------
class Account {
    private String accountNumber;
    private String ownerName;
    private double balance;

    public Account() {
        this("0000", "Unknown", 0.0);
    }

    public Account(String accountNumber, String ownerName, double balance) {
        setAccountNumber(accountNumber);
        setOwnerName(ownerName);
        setBalance(balance);
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(String accountNumber) {
        if (accountNumber == null || accountNumber.isEmpty())
            throw new IllegalArgumentException("Invalid account number");
        this.accountNumber = accountNumber;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public void setOwnerName(String ownerName) {
        if (ownerName == null || ownerName.isEmpty())
            throw new IllegalArgumentException("Invalid owner name");
        this.ownerName = ownerName;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        if (balance < 0)
            throw new IllegalArgumentException("Balance cannot be negative");
        this.balance = balance;
    }

    public void deposit(double amount) {
        if (amount <= 0)
            throw new IllegalArgumentException("Deposit must be positive");
        setBalance(getBalance() + amount);
    }

    public void withdraw(double amount) {
        if (amount <= 0)
            throw new IllegalArgumentException("Withdrawal must be positive");
        if (amount > getBalance())
            throw new IllegalArgumentException("Insufficient balance");
        setBalance(getBalance() - amount);
    }

    public void display() {
        System.out.println("================================");
        System.out.println("Account Number : " + getAccountNumber());
        System.out.println("Owner Name     : " + getOwnerName());
        System.out.printf("Balance        : Rs. %.2f%n", getBalance());
    }
}

// ---------------- SAVINGS ACCOUNT ----------------
class SavingsAccount extends Account {
    private double interestRate;

    public SavingsAccount(String accNo, String name, double balance, double interestRate) {
        super(accNo, name, balance);
        setInterestRate(interestRate);
    }

    public void setInterestRate(double interestRate) {
        if (interestRate < 0)
            throw new IllegalArgumentException("Invalid interest rate");
        this.interestRate = interestRate;
    }

    public double calculateInterest() {
        return getBalance() * interestRate / 100;
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Account Type   : Savings");
        System.out.printf("Interest Rate  : %.2f%%%n", interestRate);
        System.out.printf("Interest Earned: Rs. %.2f%n", calculateInterest());
        System.out.println("================================");
    }
}

// ---------------- CURRENT ACCOUNT ----------------
class CurrentAccount extends Account {
    private double overdraftLimit;

    public CurrentAccount(String accNo, String name, double balance, double overdraftLimit) {
        super(accNo, name, balance);
        setOverdraftLimit(overdraftLimit);
    }

    public void setOverdraftLimit(double overdraftLimit) {
        if (overdraftLimit < 0)
            throw new IllegalArgumentException("Invalid overdraft limit");
        this.overdraftLimit = overdraftLimit;
    }

    @Override
    public void withdraw(double amount) {
        if (amount <= 0)
            throw new IllegalArgumentException("Withdrawal must be positive");

        if (amount > getBalance() + overdraftLimit)
            throw new IllegalArgumentException("Exceeds overdraft limit");

        setBalance(getBalance() - amount);
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Account Type   : Current");
        System.out.printf("Overdraft Limit: Rs. %.2f%n", overdraftLimit);
        System.out.println("================================");
    }
}

// ---------------- MAIN CLASS ----------------
public class BankingSystem {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        List<Account> accounts = new ArrayList<>();

        while (true) {
            System.out.println("\n===== BANK MENU =====");
            System.out.println("1. Create Savings Account");
            System.out.println("2. Create Current Account");
            System.out.println("3. Deposit");
            System.out.println("4. Withdraw");
            System.out.println("5. Display Accounts");
            System.out.println("6. Exit");
            System.out.print("Enter choice: ");

            int choice = sc.nextInt();
            sc.nextLine(); // clear buffer

            try {
                switch (choice) {

                    case 1:
                        System.out.print("Account Number: ");
                        String sAcc = sc.nextLine();

                        System.out.print("Owner Name: ");
                        String sName = sc.nextLine();

                        System.out.print("Initial Balance: ");
                        double sBal = sc.nextDouble();

                        System.out.print("Interest Rate: ");
                        double rate = sc.nextDouble();

                        accounts.add(new SavingsAccount(sAcc, sName, sBal, rate));
                        System.out.println("Savings Account Created!");
                        break;

                    case 2:
                        System.out.print("Account Number: ");
                        String cAcc = sc.nextLine();

                        System.out.print("Owner Name: ");
                        String cName = sc.nextLine();

                        System.out.print("Initial Balance: ");
                        double cBal = sc.nextDouble();

                        System.out.print("Overdraft Limit: ");
                        double limit = sc.nextDouble();

                        accounts.add(new CurrentAccount(cAcc, cName, cBal, limit));
                        System.out.println("Current Account Created!");
                        break;

                    case 3:
                        Account depAcc = findAccount(accounts, sc);
                        if (depAcc != null) {
                            System.out.print("Amount to deposit: ");
                            double amt = sc.nextDouble();
                            depAcc.deposit(amt);
                            System.out.println("Deposit successful!");
                        }
                        break;

                    case 4:
                        Account wAcc = findAccount(accounts, sc);
                        if (wAcc != null) {
                            System.out.print("Amount to withdraw: ");
                            double amt = sc.nextDouble();
                            wAcc.withdraw(amt);
                            System.out.println("Withdrawal successful!");
                        }
                        break;

                    case 5:
                        if (accounts.isEmpty()) {
                            System.out.println("No accounts found.");
                        } else {
                            for (Account acc : accounts) {
                                acc.display();
                            }
                        }
                        break;

                    case 6:
                        System.out.println("Thank you!");
                        return;

                    default:
                        System.out.println("Invalid choice!");
                }

            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
                sc.nextLine(); // prevent crash
            }
        }
    }

    // Helper method
    public static Account findAccount(List<Account> accounts, Scanner sc) {
        System.out.print("Enter Account Number: ");
        String accNo = sc.nextLine();

        for (Account acc : accounts) {
            if (acc.getAccountNumber().equals(accNo)) {
                return acc;
            }
        }

        System.out.println("Account not found!");
        return null;
    }
}