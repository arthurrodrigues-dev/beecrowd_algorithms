package structures_and_libraries;

import java.util.*;

public class Bee1261 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numberOfWords = sc.nextInt();
        int numberOfDescriptions = sc.nextInt();
        Map<String, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < numberOfWords; i++) {
            hashMap.put(sc.next(), sc.nextInt());
        }
        sc.nextLine();

        List<List<String>> StringList = new ArrayList<>();
        
        for (int i = 0; i < numberOfDescriptions; i++) {
            List<String> text = Arrays.asList(sc.nextLine().split(" ")); 
            StringList.add(i, text);
        }

        sc.close();
        
        // salary calculation
        double salary = 0;
        for (List<String> list : StringList) {
            for (String word : list) {
                if (hashMap.containsKey(word)) {
                    salary += hashMap.get(word);
                }
            }
        }

        System.out.println(salary);
        // System.out.println(hashMap.toString());

    }
}